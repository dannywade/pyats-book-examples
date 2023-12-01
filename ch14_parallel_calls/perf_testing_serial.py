from pyats.topology.loader import load


def get_version(device):
    # Connect to device
    device.connect()
    # Parse "show version" output
    sh_ver = device.parse("show version")
    # Disconnect from device
    device.disconnect()
    # Print output
    print(sh_ver)


def main():
    # Load testbed
    testbed = load("iosv_testbed.yaml")

    # Connect to each device one by one and get version
    for dev in testbed.devices.values():
        get_version(device=dev)


if __name__ == "__main__":
    main()
    # Execution time: python perf_testing_serial.py  3.81s user 9.10s system 13% cpu 1:34.78 total
