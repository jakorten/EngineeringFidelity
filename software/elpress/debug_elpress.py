#!/usr/bin/env python3
"""
Debug EL-PRESS sensor - list all available parameters
"""

import sys
from propar import instrument

PORT = "/dev/cu.usbserial-AQ00Z5CQ"
NODE = 1  # Found on node 1

print(f"Connecting to EL-PRESS on {PORT}, node {NODE}...")

try:
    instr = instrument(PORT, NODE)
    print("Connected!\n")
except Exception as e:
    print(f"Connection failed: {e}")
    sys.exit(1)

# List all attributes
print("All available attributes:")
print("-" * 60)

attrs = [attr for attr in dir(instr) if not attr.startswith('_')]

for attr in sorted(attrs):
    try:
        value = getattr(instr, attr)
        if callable(value):
            print(f"  {attr:30s}: <method>")
        else:
            print(f"  {attr:30s}: {value}")
    except Exception as e:
        print(f"  {attr:30s}: <error: {e}>")

# Try specific pressure-related parameters
print("\n" + "=" * 60)
print("Trying pressure-related parameters:")
print("-" * 60)

pressure_params = [
    'measure', 'pressure', 'fmeasure', 'fsetpoint',
    'setpoint', 'valve_output', 'temperature',
    'init_status', 'counter_value'
]

for param in pressure_params:
    try:
        if hasattr(instr, param):
            value = getattr(instr, param)
            print(f"  {param:20s}: {value}")
    except Exception as e:
        print(f"  {param:20s}: error - {e}")

# Try reading raw parameters by number
print("\n" + "=" * 60)
print("Reading raw parameters (0-20):")
print("-" * 60)

for param_num in range(21):
    try:
        # Try to read parameter directly
        value = instr.read_parameter(param_num)
        if value is not None:
            print(f"  Param {param_num:3d}: {value}")
    except Exception as e:
        pass  # Skip errors silently
