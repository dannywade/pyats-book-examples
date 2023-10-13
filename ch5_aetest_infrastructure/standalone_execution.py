import logging
from pyats import aetest


class CommonSetup(aetest.CommonSetup):
    # Subsection 1
    @aetest.subsection
    def subsection_one(self):
        pass

    # Subsection 2
    @aetest.subsection
    def subsection_two(self):
        pass


class Testcase(aetest.Testcase):
    # Test 1
    @aetest.test
    def test_one(self):
        pass

    # Test 2
    @aetest.test
    def test_two(self):
        pass

    # Test 3
    @aetest.test
    def test_three(self):
        pass


# add the following as the absolute last block in your testscript
if __name__ == "__main__":
    # control the environment
    # eg, change some log levels for debugging
    logging.getLogger(__name__).setLevel(logging.DEBUG)
    logging.getLogger("pyats.aetest").setLevel(logging.DEBUG)

    # aetest.main() api starts the testscript execution.
    # defaults to aetest.main(testable = '__main__')
    aetest.main()


# Example Output:
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: |                            Starting common setup                             |
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: |                      Starting subsection subsection_one                      |
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: The result of subsection subsection_one is => PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: |                      Starting subsection subsection_two                      |
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: The result of subsection subsection_two is => PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: The result of common setup is => PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: |                          Starting testcase Testcase                          |
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: |                          Starting section test_one                           |
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: The result of section test_one is => PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: |                          Starting section test_two                           |
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: The result of section test_two is => PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: |                         Starting section test_three                          |
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: The result of section test_three is => PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: The result of testcase Testcase is => PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-21T00:36:15: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-21T00:36:15: %AETEST-INFO: .
# 2023-09-21T00:36:15: %AETEST-INFO: |-- common_setup                                                          PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: |   |-- subsection_one                                                    PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: |   `-- subsection_two                                                    PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: `-- Testcase                                                              PASSED
# 2023-09-21T00:36:15: %AETEST-INFO:     |-- test_one                                                          PASSED
# 2023-09-21T00:36:15: %AETEST-INFO:     |-- test_two                                                          PASSED
# 2023-09-21T00:36:15: %AETEST-INFO:     `-- test_three                                                        PASSED
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-21T00:36:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:36:15: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-21T00:36:15: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-21T00:36:15: %AETEST-INFO:  Number of ERRORED                                                            0
# 2023-09-21T00:36:15: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-21T00:36:15: %AETEST-INFO:  Number of PASSED                                                             2
# 2023-09-21T00:36:15: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-21T00:36:15: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-21T00:36:15: %AETEST-INFO:  Total Number                                                                 2
# 2023-09-21T00:36:15: %AETEST-INFO:  Success Rate                                                            100.0%
# 2023-09-21T00:36:15: %AETEST-INFO: --------------------------------------------------------------------------------
