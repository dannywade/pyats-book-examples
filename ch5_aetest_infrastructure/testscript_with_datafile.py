import logging
from genie.utils import Dq
from pyats import aetest
from unicon.core.errors import ConnectionError

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
    """Test BGP operational state"""

    @aetest.test
    def check_bgp_routes(self, testbed):
        """Check number of BGP neighbors equals expected number of routes in datafile."""

        # Print all class variables (as a Python dictionary)
        print(f"All class variables: {vars(BGPTestcase)}")
        # Example Output
        # {'__module__': '__main__', 'check_bgp_routes': <function BGPTestcase.check_bgp_routes at 0x10bf30430>, '__parameters__': {'local_asn': 65000, 'remote_asn': 65001},
        # '__doc__': None, 'source': <pyats.aetest.base.Source object at 0x10beeebb0>, '__uid__': 'routing_test_1', 'groups': ['routing'], 'expected_routes': 1, 
        # 'uid': <property object at 0x108195b30>}

        # Print available test parameters (provided by datafile) - includes TestScript and Testcase-level parameters
        print(f"Available testcase parameters: {self.parameters}")
        # Example Output
        # ParameterMap({'local_asn': 65000, 'remote_asn': 65001}, {'cloudflare_dns': '1.1.1.1', 'google_dns': '8.8.8.8', 'testbed': <Testbed object 'Cat8k Lab' at 0x108cfa490>})
        
        # Parse 'show up route bgp' command output using Genie parsers
        r1_bgp_routes = testbed.devices["cat8k-rt1"].parse("show ip route bgp")
        r2_bgp_routes = testbed.devices["cat8k-rt2"].parse("show ip route bgp")

        # Capture the number of BGP routes in the routing table using the Genie Dq library
        self.r1_route_count = (
            len(Dq(r1_bgp_routes).contains("routes").get_values("route"))
        )
        self.r2_route_count = (
            len(Dq(r2_bgp_routes).contains("routes").get_values("route"))
        )

        # Confirm number of BGP routes equals the expected number of routes provided as a class variable in the datafile
        if self.r1_route_count == self.expected_routes:
            self.passed(
                "There were the correct number of expected BGP routes on router 1."
            )
        else:
            self.failed(f"Router 1 does not have the expected number of BGP routes ({self.expected_routes}). Instead, there are {self.r1_route_count} BGP routes.")
        if self.r2_route_count == self.expected_routes:
            self.passed(
                "There were the correct number of expected BGP routes on router 2."
            )
        else:
            self.failed(f"Router 2 does not have the expected number of BGP routes ({self.expected_routes}). Instead, there are {self.r2_route_count} BGP routes.")


class ExternalConnectivity(aetest.Testcase):
    """Test external connectivity by pinging external DNS servers (Google and Cloudflare) using pyATS device Ping API.
    
    There are no pass/fail conditions in this testcase, as the goal is to illustrate the use of datafile input parameters. All tests will pass.
    """

    @aetest.test
    def ping_cloudflare_dns(self, testbed):
        """Ping Cloudflare DNS servers"""

        # Print all TestScript-level parameters - you'll notice the BGPTestcase parameters are not included, as they are Testcase-level parameters
        # You'll also notice the addition of the 'alt_google_dns' parameter, as that is a Testcase-level parameter
        print(self.parameters)
        # Example Output
        # ParameterMap({'alt_google_dns': '8.8.4.4'}, {'cloudflare_dns': '1.1.1.1', 'google_dns': '8.8.8.8', 'testbed': <Testbed object 'Cat8k Lab' at 0x10a485310>})

        # Use 'cloudflare_dns' TestScript-level parameter to ping Cloudflare DNS servers (found in base.yaml)
        testbed.devices["cat8k-rt1"].api.ping(self.parameters["cloudflare_dns"])

    @aetest.test
    def ping_google_dns(self, testbed):
        """Ping Google DNS servers"""

        # Use 'google_dns' TestScript-level parameter and 'alt_google_dns' Testcase-level parameter to ping Google DNS servers (both found in datafile.yaml)
        testbed.devices["cat8k-rt1"].api.ping(self.parameters["google_dns"])
        testbed.devices["cat8k-rt1"].api.ping(self.parameters["alt_google_dns"])

class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        """Disconnect from all devices"""
        testbed.disconnect()
        logger.info(f"Disconnected from all devices in {testbed.name}")

if __name__ == "__main__":

    from pyats.topology.loader import load

    # Load testbed object from testbed file
    tb = load("../testbed.yaml")
    # Run with standalone execution
    aetest.main(datafile="datafile.yaml", testbed=tb)


# Example Output (Results section only for brevity):
# 2023-09-24T12:59:27: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T12:59:27: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-24T12:59:27: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T12:59:27: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
# 2023-09-24T12:59:27: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-24T12:59:27: %AETEST-INFO: .
# 2023-09-24T12:59:27: %AETEST-INFO: |-- common_setup                                                          PASSED
# 2023-09-24T12:59:27: %AETEST-INFO: |   `-- connect_to_devices                                                PASSED
# 2023-09-24T12:59:27: %AETEST-INFO: |-- routing_test_1                                                        PASSED
# 2023-09-24T12:59:27: %AETEST-INFO: |   `-- check_bgp_routes                                                  PASSED
# 2023-09-24T12:59:27: %AETEST-INFO: |-- ext_test_dns                                                          PASSED
# 2023-09-24T12:59:27: %AETEST-INFO: |   |-- ping_cloudflare_dns                                               PASSED
# 2023-09-24T12:59:27: %AETEST-INFO: |   `-- ping_google_dns                                                   PASSED
# 2023-09-24T12:59:27: %AETEST-INFO: `-- common_cleanup                                                        PASSED
# 2023-09-24T12:59:27: %AETEST-INFO:     `-- disconnect_from_devices                                           PASSED
# 2023-09-24T12:59:27: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T12:59:27: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-24T12:59:27: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T12:59:27: %AETEST-INFO:  Number of ABORTED                                                            0 
# 2023-09-24T12:59:27: %AETEST-INFO:  Number of BLOCKED                                                            0 
# 2023-09-24T12:59:27: %AETEST-INFO:  Number of ERRORED                                                            0 
# 2023-09-24T12:59:27: %AETEST-INFO:  Number of FAILED                                                             0 
# 2023-09-24T12:59:27: %AETEST-INFO:  Number of PASSED                                                             4 
# 2023-09-24T12:59:27: %AETEST-INFO:  Number of PASSX                                                              0 
# 2023-09-24T12:59:27: %AETEST-INFO:  Number of SKIPPED                                                            0 
# 2023-09-24T12:59:27: %AETEST-INFO:  Total Number                                                                 4 
# 2023-09-24T12:59:27: %AETEST-INFO:  Success Rate                                                            100.0% 