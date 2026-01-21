#!/usr/bin/env python3
"""
EL-PRESS Tare/Zero Script
Applies software offset to zero the sensor at current atmospheric pressure
"""

import sys
import time
import json
from pathlib import Path
from propar import instrument

PORT = "/dev/cu.usbserial-AQ00Z5CQ"
NODE = 4
OFFSET_FILE = Path(__file__).parent / "elpress_offset.json"


def get_current_reading(instr, samples: int = 10) -> float:
    """Get averaged current reading"""
    readings = []
    for _ in range(samples):
        val = instr.measure
        if val is not None:
            readings.append(float(val))
        time.sleep(0.1)

    if not readings:
        raise RuntimeError("Could not read sensor")

    return sum(readings) / len(readings)


def load_offset() -> float:
    """Load saved offset from file"""
    if OFFSET_FILE.exists():
        with open(OFFSET_FILE) as f:
            data = json.load(f)
            return data.get('offset', 0.0)
    return 0.0


def save_offset(offset: float):
    """Save offset to file"""
    with open(OFFSET_FILE, 'w') as f:
        json.dump({
            'offset': offset,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        }, f, indent=2)
    print(f"Offset saved to {OFFSET_FILE}")


def tare(instr):
    """Tare the sensor (set current reading as zero)"""
    print("Taring sensor...")
    print("Ensure sensor is at atmospheric pressure (no applied pressure)")
    print("Averaging 10 readings...")

    current = get_current_reading(instr, samples=10)
    print(f"Current reading: {current:.2f} mbar")

    save_offset(current)
    print(f"Offset set to: {current:.2f} mbar")
    print("Future readings will be corrected by this offset.")


def read_with_offset(instr) -> float:
    """Read pressure with offset correction"""
    offset = load_offset()
    raw = instr.measure
    if raw is not None:
        return float(raw) - offset
    return None


def main():
    print("=" * 50)
    print("EL-PRESS Tare Utility")
    print("=" * 50)

    instr = instrument(PORT, NODE)
    print(f"Connected to {PORT}, node {NODE}\n")

    # Show current state
    offset = load_offset()
    raw = instr.measure
    corrected = float(raw) - offset if raw else None

    print(f"Current offset: {offset:.2f} mbar")
    print(f"Raw reading:    {raw} mbar")
    print(f"Corrected:      {corrected:.2f} mbar" if corrected else "Corrected: N/A")

    if len(sys.argv) > 1 and sys.argv[1] == "--tare":
        print("\n" + "-" * 50)
        tare(instr)
    else:
        print("\nUsage:")
        print("  python tare_elpress.py          # Show current readings")
        print("  python tare_elpress.py --tare   # Tare the sensor")

    # Show corrected readings
    print("\n" + "-" * 50)
    print("Live corrected readings (Ctrl+C to stop):")
    print(f"{'Raw':>10} {'Offset':>10} {'Corrected':>10}")

    try:
        while True:
            raw = instr.measure
            offset = load_offset()
            if raw is not None:
                corrected = float(raw) - offset
                print(f"{raw:10.2f} {offset:10.2f} {corrected:10.2f} mbar")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nDone.")


if __name__ == "__main__":
    main()
