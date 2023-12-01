from pyats.topology.loader import load
from pyats.async_ import pcall


def get_version(device):
    # Connect to device
    device.connect()
    # Parse "show version" output
    sh_ver = device.parse("show version")
    # Disconnect from device
    device.disconnect()
    # Print and return output
    print(sh_ver)
    return sh_ver


def main():
    # Load testbed
    testbed = load("iosv_testbed.yaml")

    # List of all device objects from testbed
    tb_devices = testbed.devices.values()
    # [<Device ios-sw1 at 0x1142c3640>, <Device ios-sw2 at 0x1142c3610>, <Device ios-sw3 at 0x1142ba820>, <Device ios-sw4 at 0x1142bab50>, <Device ios-sw5 at 0x114633430>]

    # Connect and get version of each testbed device in parallel
    # Results must be a pickleable object. In this case, we are returning a dict type
    version_results = pcall(get_version, device=tb_devices)

    # All results are stored in a tuple
    print(f"SHOW VERSION OUTPUT:\n {version_results}")


if __name__ == "__main__":
    main()
    # Execution time: python perf_testing_pcall.py  9.74s user 12.54s system 70% cpu 31.799 total
