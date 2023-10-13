from pyats.topology.loader import load

# Load testbed and select cat8k-rt1 device
my_testbed = load("testbed.yaml")
xe_router = my_testbed.devices["cat8k-rt1"]
xe_router.connect()
# Configure hostname and disable console logging with a multiline string
xe_router.configure(
    """
    hostname cat8k-1 
    no logging console 
"""
)

# Configure logging hosts with a list
cmd = ["logging host 10.1.1.1", "logging host 10.1.1.2"]
xe_router.configure(cmd, timeout=30)
xe_router.disconnect()
