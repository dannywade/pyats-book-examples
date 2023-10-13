from genie.libs.filetransferutils import FileServer
from pyats.topology.loader import load

# Load testbed and select “cat8k-rt1” device
my_testbed = load("testbed.yaml")
xe_router = my_testbed.devices["cat8k-rt1"]

# Instantiate file server in script instead of defining in testbed
with FileServer(
    protocol="ftp", path="/path/to/root/dir", testbed=my_testbed, name="mycontextserver"
) as fs:
    xe_router.api.copy_to_device(
        protocol="ftp",
        server="mycontextserver",
        remote_path="myimage.bin",
        local_path="flash:/",
    )
