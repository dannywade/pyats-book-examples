# The OS choices are - nxos; iosxr; iosxe - For this example, we will be
# using nxos
from genie import testbed
from genie.libs.ops.bgp.iosxe.bgp import Bgp

# Load Genie testbed
testbed = testbed.load(testbed="testbed.yaml")

# Find the device using hostname or alias
uut = testbed.devices["cat8k-rt2"]
uut.connect()

# Instantiate the Ops object
bgp_obj = Bgp(device=uut)

# This will send many show command to learn the operational state
# of interfaces for this device
bgp_obj.learn()

import pprint

pprint.pprint(bgp_obj.info)
