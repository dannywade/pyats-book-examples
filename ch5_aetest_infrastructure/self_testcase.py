from pyats import aetest


class L2Testcase(aetest.Testcase):
    @aetest.setup
    def collect_l2_info(self, device):
        # Collect MAC address table entries
        self.mac_table = device.execute("show mac-address table")

    @aetest.test
    def confirm_mac_addresses(self):
        # Confirm the "important" MAC address is found in the MAC address
        important_mac = "0123.4567.0987"
        assert important_mac in self.mac_table


if __name__ == "__main__":
    # Must run with testbed
    # from pyats.topology.loader import load

    # Load testbed object from testbed YAML file
    # tb = load("testbed.yaml")
    # aetest.main(testbed=tb)
    pass
