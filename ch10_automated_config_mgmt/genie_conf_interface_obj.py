from pyats.topology.loader import load
from genie.conf.base import Interface


# Load testbed and select “cat8k-rt1” device
my_testbed = load("testbed.yaml")
xe_router = my_testbed.devices["cat8k-rt1"]

# Create “GigabitEthernet4” Interface object for cat8k-rt1 device
xe_interface = Interface(device=xe_router, name="GigabitEthernet4")

# Set interface attributes
xe_interface.ipv4 = "10.1.1.1"
xe_interface.ipv4.netmask = "255.255.255.0"
xe_interface.shutdown = False


# To find out more about the different Interface attributes, do one of the following:
# print(dir(xe_interface))
# Check out the Interface object source code on GitHub: https://github.com/CiscoTestAutomation/genielibs/blob/master/pkgs/conf-pkg/src/genie/libs/conf/interface/__init__.py#L187

# Build config (without pushing configuration to the device)
print(xe_interface.build_config(apply=False))

# Build and push config to device
xe_interface.build_config()

# Remove the config from the device
xe_interface.build_unconfig()
