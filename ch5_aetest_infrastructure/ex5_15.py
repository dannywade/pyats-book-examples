import logging
from genie.utils import Dq
from pyats import aetest
from unicon.core.errors import ConnectionError
import time

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all testbed devices"""
        try:
            testbed.connect()
        except ConnectionError:
            self.failed(f"Could not connect to all devices in {testbed.name}")
        # Print log message confirming all devices are in a 'connected' state
        logger.info(f"Connected to all devices in {testbed.name}")


class BGPTestcase(aetest.Testcase):
    @aetest.test
    def check_bgp_routes(self, testbed, expected_routes):
        """Check number of BGP neighbors equals expected number of routes in datafile."""
        # Parse BGP routes
        r1_bgp_routes = testbed.devices["cat8k-rt1"].parse("show ip route bgp")
        r2_bgp_routes = testbed.devices["cat8k-rt2"].parse("show ip route bgp")

        # Capture the number of BGP routes in the routing table
        self.r1_route_count = (
            Dq(r1_bgp_routes).contains("routes").get_values("route").count()
        )
        self.r2_route_count = (
            Dq(r2_bgp_routes).contains("routes").get_values("route").count()
        )

        # Confirm number of BGP routes equals the expected number of routes provided as a test parameter in the datafile
        if self.r1_route_count == expected_routes:
            self.passed(
                "There were the correct number of expected BGP routes on router 1."
            )
        else:
            self.failed("Router 1 does not have the expected number of BGP routes.")
        if self.r2_route_count == expected_routes:
            self.passed(
                "There were the correct number of expected BGP routes on router 2."
            )
        else:
            self.failed("Router 2 does not have the expected number of BGP routes.")
