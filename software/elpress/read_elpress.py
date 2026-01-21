#!/usr/bin/env python3
"""
EL-PRESS Pressure Sensor Reader
Bronkhorst EL-PRESS P-502C via RS232 (USB adapter)

Uses PROPAR protocol via propar library.

Usage:
    python read_elpress.py                    # Single reading
    python read_elpress.py -c 10              # Continuous for 10 seconds
    python read_elpress.py -c 10 -o data.csv  # Save to CSV
    python read_elpress.py --scan             # Find sensor node
    python read_elpress.py --raw              # Without tare offset

Configuration:
    Port: /dev/cu.usbserial-AQ00Z5CQ
    Node: 4
    Protocol: PROPAR (38400 baud)

Calibration:
    Run tare_elpress.py --tare to zero the sensor after 30 min warm-up.
"""

import sys
import time
import json
import signal
import argparse
from pathlib import Path
from datetime import datetime

# Configuration
DEFAULT_PORT = "/dev/cu.usbserial-AQ00Z5CQ"
DEFAULT_NODE = 4
OFFSET_FILE = Path(__file__).parent / "elpress_offset.json"

# Global for clean shutdown
_running = True


def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    global _running
    _running = False
    print("\nStopping...")


signal.signal(signal.SIGINT, signal_handler)


def check_propar() -> bool:
    """Check if propar library is available"""
    try:
        import propar
        return True
    except ImportError:
        print("ERROR: propar library not installed")
        print("Install with: pip install propar")
        print("Or use: source venv/bin/activate")
        return False


def connect(port: str, node: int):
    """Connect to EL-PRESS sensor

    Args:
        port: Serial port path
        node: PROPAR node address

    Returns:
        propar.instrument or None on failure
    """
    from propar import instrument

    try:
        instr = instrument(port, node)
        time.sleep(0.2)  # Allow connection to stabilize
        # Verify connection by attempting a read
        _ = instr.readParameter(175)  # Read ident (more reliable than measure)
        return instr
    except Exception as e:
        print(f"Connection failed: {e}")
        return None


def load_offset() -> float:
    """Load saved tare offset from file

    Returns:
        Offset value in mbar, or 0.0 if no offset file exists
    """
    if OFFSET_FILE.exists():
        try:
            with open(OFFSET_FILE) as f:
                data = json.load(f)
                return float(data.get('offset', 0.0))
        except (json.JSONDecodeError, ValueError, KeyError):
            print(f"Warning: Could not read offset from {OFFSET_FILE}")
    return 0.0


def read_pressure(instr, apply_offset: bool = True) -> float | None:
    """Read gauge pressure from EL-PRESS

    Args:
        instr: propar.instrument object
        apply_offset: If True, subtract tare offset

    Returns:
        Pressure in mbar (gauge), or None on error
    """
    try:
        value = instr.measure
        if value is None:
            return None

        pressure = float(value)

        if apply_offset:
            offset = load_offset()
            pressure -= offset

        return pressure

    except Exception as e:
        print(f"Read error: {e}")
        return None


def scan_nodes(port: str, nodes: list[int] | None = None) -> tuple[int | None, any]:
    """Scan for sensor on different node addresses

    Args:
        port: Serial port path
        nodes: List of node addresses to try (default: common addresses)

    Returns:
        Tuple of (node_address, instrument) or (None, None) if not found
    """
    from propar import instrument

    if nodes is None:
        nodes = [1, 2, 3, 4, 5, 6, 7, 8, 128]

    print(f"Scanning for sensor on {port}...")

    for node in nodes:
        print(f"  Node {node:3d}...", end=" ", flush=True)
        try:
            instr = instrument(port, node)
            measure = instr.measure
            if measure is not None:
                print(f"FOUND (measure={measure})")
                return node, instr
            else:
                print("no data")
        except Exception:
            print("no response")

    return None, None


def continuous_read(
    instr,
    duration: float,
    interval: float,
    apply_offset: bool = True,
    output_file: str | None = None
) -> list[tuple[float, float]]:
    """Continuous pressure reading with optional CSV output

    Args:
        instr: propar.instrument object
        duration: How long to read (seconds)
        interval: Time between readings (seconds)
        apply_offset: If True, subtract tare offset
        output_file: Optional CSV file path for output

    Returns:
        List of (timestamp, pressure) tuples
    """
    global _running
    _running = True

    offset = load_offset() if apply_offset else 0.0

    print(f"\nContinuous reading for {duration}s (interval {interval}s)")
    if apply_offset and offset != 0.0:
        print(f"Tare offset: {offset:.1f} mbar")
    print("-" * 55)
    print(f"{'Time (s)':>10} {'Raw (mbar)':>12} {'Corrected':>12} {'Status':>10}")
    print("-" * 55)

    # Open CSV file if requested
    csv_file = None
    if output_file:
        csv_file = open(output_file, 'w')
        csv_file.write("timestamp_s,raw_mbar,corrected_mbar\n")

    start_time = time.time()
    readings = []

    while _running and (time.time() - start_time) < duration:
        elapsed = time.time() - start_time

        try:
            raw = instr.measure
            if raw is not None:
                raw = float(raw)
                corrected = raw - offset
                readings.append((elapsed, corrected))

                print(f"{elapsed:10.2f} {raw:12.1f} {corrected:12.1f} {'OK':>10}")

                if csv_file:
                    csv_file.write(f"{elapsed:.3f},{raw:.1f},{corrected:.1f}\n")
            else:
                print(f"{elapsed:10.2f} {'--':>12} {'--':>12} {'NO DATA':>10}")

        except Exception as e:
            print(f"{elapsed:10.2f} {'--':>12} {'--':>12} {'ERROR':>10}")

        # Sleep for interval, but check _running periodically
        sleep_until = time.time() + interval
        while _running and time.time() < sleep_until:
            time.sleep(0.01)

    print("-" * 55)

    if csv_file:
        csv_file.close()
        print(f"Data saved to: {output_file}")

    # Statistics
    if readings:
        pressures = [p for _, p in readings]
        print(f"\nStatistics ({len(readings)} readings):")
        print(f"  Min: {min(pressures):8.1f} mbar")
        print(f"  Max: {max(pressures):8.1f} mbar")
        print(f"  Avg: {sum(pressures)/len(pressures):8.1f} mbar")
        if len(pressures) > 1:
            print(f"  Range: {max(pressures) - min(pressures):8.1f} mbar")

    return readings


def get_sensor_info(instr) -> dict:
    """Get sensor identification info

    Returns:
        Dict with available sensor attributes
    """
    info = {}
    attrs = [
        'serial_number', 'model_number', 'fluid_name',
        'capacity', 'capacity_unit', 'user_tag'
    ]

    for attr in attrs:
        try:
            if hasattr(instr, attr):
                value = getattr(instr, attr)
                if value is not None:
                    info[attr] = value
        except Exception:
            pass

    # Also try to get identification number
    try:
        ident = instr.readParameter(175)
        if ident is not None:
            info['ident_nr'] = ident
    except Exception:
        pass

    return info


def main():
    parser = argparse.ArgumentParser(
        description="Read Bronkhorst EL-PRESS pressure sensor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python read_elpress.py                    Single reading
  python read_elpress.py -c 60              Read for 60 seconds
  python read_elpress.py -c 60 -i 0.05      Read at 20 Hz for 60 seconds
  python read_elpress.py -c 60 -o data.csv  Save to CSV file
  python read_elpress.py --scan             Find sensor node address
  python read_elpress.py --raw              Read without tare offset
        """
    )

    parser.add_argument(
        "port", nargs="?", default=DEFAULT_PORT,
        help=f"Serial port (default: {DEFAULT_PORT})"
    )
    parser.add_argument(
        "-n", "--node", type=int, default=DEFAULT_NODE,
        help=f"Node address (default: {DEFAULT_NODE})"
    )
    parser.add_argument(
        "-s", "--scan", action="store_true",
        help="Scan for sensor on different nodes"
    )
    parser.add_argument(
        "-c", "--continuous", type=float, default=0, metavar="SECONDS",
        help="Continuous reading duration in seconds"
    )
    parser.add_argument(
        "-i", "--interval", type=float, default=0.1, metavar="SECONDS",
        help="Reading interval in seconds (default: 0.1)"
    )
    parser.add_argument(
        "-o", "--output", type=str, metavar="FILE",
        help="Output CSV file for continuous readings"
    )
    parser.add_argument(
        "--raw", action="store_true",
        help="Show raw values without tare offset"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true",
        help="Show additional sensor info"
    )

    args = parser.parse_args()

    # Check dependencies
    if not check_propar():
        return 1

    print("=" * 55)
    print("EL-PRESS Pressure Sensor Reader")
    print("=" * 55)

    # Scan mode
    if args.scan:
        node, instr = scan_nodes(args.port)
        if instr is None:
            print("\nNo sensor found!")
            return 1
        print(f"\nUse: python read_elpress.py -n {node}")
    else:
        # Direct connection
        print(f"Connecting to {args.port}, node {args.node}...", end=" ", flush=True)
        instr = connect(args.port, args.node)
        if instr is None:
            print("FAILED")
            print("\nTry: python read_elpress.py --scan")
            return 1
        print("OK")

    # Show sensor info
    if args.verbose:
        print("\nSensor Info:")
        info = get_sensor_info(instr)
        if info:
            for key, value in info.items():
                print(f"  {key}: {value}")
        else:
            print("  (no info available)")

    # Show offset status
    offset = load_offset()
    apply_offset = not args.raw
    if offset != 0.0:
        print(f"\nTare offset: {offset:.1f} mbar", end="")
        print(" (applied)" if apply_offset else " (--raw: not applied)")
    elif not args.raw:
        print("\nNo tare offset set. Run: python tare_elpress.py --tare")

    # Read
    if args.continuous > 0:
        continuous_read(
            instr,
            duration=args.continuous,
            interval=args.interval,
            apply_offset=apply_offset,
            output_file=args.output
        )
    else:
        # Single reading with retry
        print("\nPressure reading:")
        raw = None
        for attempt in range(3):
            raw = instr.measure
            if raw is not None:
                break
            time.sleep(0.1)

        if raw is not None:
            raw = float(raw)
            corrected = raw - offset if apply_offset else raw
            print(f"  Raw:       {raw:8.1f} mbar")
            if apply_offset and offset != 0.0:
                print(f"  Offset:    {offset:8.1f} mbar")
                print(f"  Corrected: {corrected:8.1f} mbar")
        else:
            print("  ERROR: Could not read pressure (3 attempts failed)")
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
