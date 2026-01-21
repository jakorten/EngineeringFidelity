#!/usr/bin/env python3
"""
Debug EL-PRESS sensor v2 - read specific pressure parameters
"""

import sys
import time
import propar
from propar import instrument

PORT = "/dev/cu.usbserial-AQ00Z5CQ"
NODE = 1

print(f"Connecting to EL-PRESS on {PORT}, node {NODE}...")

try:
    instr = instrument(PORT, NODE)
    print("Connected!\n")
except Exception as e:
    print(f"Connection failed: {e}")
    sys.exit(1)

# Key parameters for pressure sensors from parameters.py
PARAMS = {
    8: "fmeasure (flow measure)",
    21: "measure",
    33: "process (fmeasure/fsetpoint process)",
    60: "monitor",
    106: "PressSensr (pressure sensor type)",
    107: "BaroPress (barometer pressure)",
    143: "pressure (absolute pressure in mbar)",
    153: "delta-p (relative pressure)",
    175: "IdentNr (identification number)",
}

print("Reading key parameters:")
print("-" * 60)

for param_id, description in PARAMS.items():
    try:
        # Use readParameter method
        value = instr.readParameter(param_id)
        print(f"  Param {param_id:3d} ({description}): {value}")
    except Exception as e:
        print(f"  Param {param_id:3d} ({description}): error - {e}")

# Try different process numbers
print("\n" + "=" * 60)
print("Trying to read using read_parameters:")
print("-" * 60)

try:
    # Read fmeasure (8) and fsetpoint (9) from process 33
    params = instr.read_parameters([
        {'proc_nr': 33, 'parm_nr': 8, 'parm_type': propar.PP_TYPE_FLOAT},
    ])
    print(f"  Process 33, param 8: {params}")
except Exception as e:
    print(f"  Error: {e}")

# Scan more nodes to find the right device
print("\n" + "=" * 60)
print("Scanning all nodes (1-10, 128):")
print("-" * 60)

for node in list(range(1, 11)) + [128]:
    try:
        test_instr = instrument(PORT, node)

        # Try to read identification
        ident = test_instr.readParameter(175)  # IdentNr
        measure = test_instr.measure

        if ident is not None or measure is not None:
            print(f"  Node {node:3d}: ident={ident}, measure={measure}")

            # If found, try pressure params
            try:
                pressure = test_instr.readParameter(143)
                deltap = test_instr.readParameter(153)
                print(f"           pressure={pressure}, delta-p={deltap}")
            except:
                pass
    except Exception as e:
        pass  # Skip nodes with no response

print("\nDone.")
