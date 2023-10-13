from pyats.topology.loader import load

tb = load("testbed.yaml")
# Connect to all testbed devices
tb.connect()
# Configure logging host on all testbed devices
tb.configure("logging host 10.1.1.1")
# Disconnect from all testbed devices
tb.disconnect()
