#!/usr/bin/env python3
"""
EL-PRESS Diagnostic Script
Shows all relevant readings to help identify correct pressure value
"""

import time
from propar import instrument

PORT = "/dev/cu.usbserial-AQ00Z5CQ"
NODE = 4

print("=" * 60)
print("EL-PRESS P-502C Diagnostic")
print("=" * 60)

instr = instrument(PORT, NODE)
print(f"Connected to {PORT}, node {NODE}\n")

# Read all relevant parameters
print("Current readings:")
print("-" * 60)

# Primary measurement
measure = instr.measure
print(f"  measure:        {measure}")

# Setpoint (for controllers)
setpoint = instr.setpoint
print(f"  setpoint:       {setpoint}")

# Delta-P (relative pressure)
delta_p = instr.readParameter(153)
print(f"  delta-p (153):  {delta_p} bar = {delta_p*1000 if delta_p else 'N/A'} mbar")

# Capacity/range
capacity = instr.readParameter(21)
print(f"  capacity (21):  {capacity}")

# Identification
ident = instr.readParameter(175)
print(f"  ident (175):    {ident}")

# Try fmeasure
fmeasure = instr.readParameter(8)
print(f"  fmeasure (8):   {fmeasure}")

print("\n" + "=" * 60)
print("Interpretation:")
print("-" * 60)

if measure is not None:
    print(f"\n  If 'measure' is gauge pressure:")
    print(f"    → Current pressure = {measure:.1f} mbar")
    print(f"    → (Expected: ~0 mbar at rest, up to 100 mbar under pressure)")

if delta_p is not None:
    print(f"\n  If 'delta-p' is atmospheric reference:")
    print(f"    → Atmospheric = {delta_p*1000:.1f} mbar ({delta_p:.4f} bar)")
    print(f"    → (Expected: ~1013 mbar)")

print("\n" + "=" * 60)
print("Live readings (press Ctrl+C to stop):")
print("-" * 60)
print(f"{'Time':>8}  {'measure':>10}  {'delta-p':>12}")

try:
    start = time.time()
    while True:
        m = instr.measure
        d = instr.readParameter(153)
        t = time.time() - start
        m_str = f"{m:10.1f}" if m is not None else "       N/A"
        d_str = f"{d*1000:12.1f}" if d is not None else "         N/A"
        print(f"{t:8.1f}  {m_str}  {d_str} mbar")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nStopped.")
