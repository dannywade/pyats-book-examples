from pyats import aetest
import genie
from genie.harness.standalone import GenieStandalone, run_genie_sdk


class CommonSetup(aetest.CommonSetup):
    """Common Setup section"""

    @aetest.subsection
    def connect(self, testbed):
        """Connect to each device in the testbed."""

        genie_testbed = genie.testbed.load(testbed)
        self.parent.parameters["testbed"] = genie_testbed
        genie_testbed.connect()


# Call Triggers and Verifications as independent pyATS testcase
class GenieOspfTriggerVerification(GenieStandalone):
    """Shut/unshut the OSPF process and verify LSA Type 1 packets are still being exchanged before and after testing."""

    # Must specify 'uut' - If other devices are included in the datafile(s), they will also be tested
    uut = "iosv-0"
    triggers = ["TriggerShutNoShutOspf"]
    verifications = ["Verify_IpOspfDatabaseRouter"]


# Calling Triggers and Verifications within a pyATS section
class tc_pyats_genie(aetest.Testcase):
    """Testcase with triggers and verifications."""

    # First test section
    @aetest.test
    def simple_test_1(self, steps):
        """Sample test section."""

        # Run Genie triggers and verifications
        # Note that you must specify the order of each trigger and verification
        run_genie_sdk(
            self,
            steps,
            [
                "Verify_IpOspfDatabaseRouter",
                "TriggerShutNoShutOspf",
                "Verify_IpOspfDatabaseRouter",
            ],
            uut="iosv-0",
        )


class CommonCleanup(aetest.CommonCleanup):
    """Common Cleanup section"""

    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        """Disconnect from each device in the testbed."""
        testbed.disconnect()
