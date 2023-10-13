from pyats.topology.loader import load

# Load testbed and select “cat8k-rt1” device
my_testbed = load("testbed.yaml")
xe_router = my_testbed.devices["cat8k-rt1"]

# Copy myimage.bin to flash:/ on router via FTP
xe_router.api.copy_to_device(
    protocol="ftp",
    server="myftpserver",
    remote_path="myimage.bin",
    local_path="flash:/",
)
