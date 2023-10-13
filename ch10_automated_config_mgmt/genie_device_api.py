from pyats.topology.loader import load

# Load testbed and select cat8k-rt1 device
my_testbed = load("testbed.yaml")
xe_router = my_testbed.devices["cat8k-rt1"]
# Connect to cat8k-rt1
xe_router.connect()

# Shut Loopback0 interface
xe_router.api.shut_interface(interface="Loopback0")
# Check the config of Loopback0 interface
xe_router.api.get_interface_config(interface="Loopback0")
# Unshut Loopback0 interface
xe_router.api.unshut_interface(interface="Loopback0")

# Disconnect from the device
xe_router.disconnect()
