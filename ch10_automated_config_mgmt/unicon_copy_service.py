from pyats.topology.loader import load

# Load testbed and select “cat8k-rt1” device
my_testbed = load("testbed.yaml")
xe_router = my_testbed.devices["cat8k-rt1"]

# Saving running-config to startup-config on router
out = xe_router.copy(source="running-conf", dest="startup-config")

# Copy 'copy-test.txt' file from TFTP server to bootflash on router
out = xe_router.copy(
    source="tftp:",
    dest="bootflash:",
    source_file="copy-test.txt",
    dest_file="copy-test.txt",
    server="10.105.33.158",
)
