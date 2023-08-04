from genie import testbed
from genie.libs.conf.interface.iosxe.interface import Interface
import pprint

# Load Genie testbed
testbed = testbed.load(testbed="testbed.yaml")

# Find the device using hostname or alias
uut = testbed.devices["cat8k-rt2"]

# Instantiate the Conf object
interface_obj = Interface(device=uut, name="Loopback100")

# Add attributes to the Interface object
interface_obj.description = "Managed by pyATS"
interface_obj.ipv4 = "1.1.1.1"
interface_obj.ipv4.netmask = "255.255.255.255"
interface_obj.shutdown = False

# Build the configuration for the interface
print(interface_obj.build_config(apply=False))
