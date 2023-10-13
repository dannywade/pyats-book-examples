from pyats.utils.fileutils import FileUtils
from pyats.topology.loader import load

tb = load("testbed.yaml")


# This with statement ensures that any sessions are automatically closed
# if something goes wrong.
with FileUtils(testbed=tb) as futils:
    # Copy local file to remote location (note the two ways of specifying server name):
    futils.copyfile(
        source="/local/path/to/file",
        destination="ftp://server_alias/remote/path/to/file",
    )

    futils.copyfile(
        source="file:///local/path/to/file",
        destination="tftp://myserver.domain.com/remote/path/to/file",
        timeout_seconds=80,
    )

    # Copy remote file to local location, specifying the server via its address:
    futils.copyfile(
        source="scp://1.1.1.1/path/to/file", destination="/local/path/to/file"
    )
