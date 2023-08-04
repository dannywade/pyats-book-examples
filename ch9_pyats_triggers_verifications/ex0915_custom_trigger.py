import time
import logging
from pyats import aetest

from genie.harness.base import Trigger
from genie.metaparser.util.exceptions import SchemaEmptyParserError

log = logging.getLogger()


class MyShutNoShutOspf(Trigger):
    """Shut and unshut OSPF process. Verify both actions."""

    @aetest.setup
    def prerequisites(self, uut):
        """Check whether OSPF is configured and running."""

        # Checks if OSPF is configured. If not, skip this trigger
        try:
            output = uut.parse("show ip ospf")
        except SchemaEmptyParserError:
            self.failed(f"OSPF is not configured on device {uut.name}")

        # Extract the OSPF process ID - this will be used throughout the trigger
        self.ospf_id = list(
            output["vrf"]["default"]["address_family"]["ipv4"]["instance"].keys()
        )[0]

        # Checks if the OSPF process is enabled
        ospf_enabled = output["vrf"]["default"]["address_family"]["ipv4"]["instance"][
            self.ospf_id
        ]["enable"]

        if not ospf_enabled:
            self.skipped(f"OSPF is not enabled on device {uut.name}")

    @aetest.test
    def ShutOspf(self, uut):
        """Shutdown the OSPF process"""

        uut.configure(f"router ospf {self.ospf_id}\n shutdown")
        time.sleep(5)

    @aetest.test
    def verify_ShutOspf(self, uut):
        """Verify ShutOspf worked"""

        output = uut.parse("show ip ospf")

        ospf_enabled = output["vrf"]["default"]["address_family"]["ipv4"]["instance"][
            self.ospf_id
        ]["enable"]

        if ospf_enabled:
            self.failed(f"OSPF is enabled on device {uut.name}")

    @aetest.test
    def NoShutOspf(self, uut):
        """Unshut the OSPF process"""

        uut.configure(f"router ospf {self.ospf_id}\n no shutdown")

    @aetest.test
    def verify_NoShutOspf(self, uut):
        """Verify NoShutOspf worked"""

        output = uut.parse("show ip ospf")

        ospf_enabled = output["vrf"]["default"]["address_family"]["ipv4"]["instance"][
            self.ospf_id
        ]["enable"]

        if not ospf_enabled:
            self.failed(f"OSPF is enabled on device {uut.name}")
