from pyats import aetest


class CommonSetup(aetest.CommonSetup):
    @aetest.subsection
    def subsection(self):
        # goto with a message
        self.errored("setup error, abandoning script", goto=["exit"])


# --------------------------------------------------------------------------
class TestcaseOne(aetest.Testcase):
    @aetest.setup
    def setup(self):
        # setup failed, go to cleanup of testcase
        self.failed("test failed", goto=["cleanup"])


# --------------------------------------------------------------------------
class TestcaseTwo(aetest.Testcase):
    # test failed, move onto next testcase
    @aetest.test
    def test(self):
        self.failed(goto=["next_tc"])


# --------------------------------------------------------------------------
class TestcaseThree(aetest.Testcase):
    @aetest.setup
    def setup(self):
        # setup failed, move onto cleanup of this testcase, then
        # jump to common_cleanup directly.
        self.failed(goto=["cleanup", "common_cleanup"])


if __name__ == "__main__":
    aetest.main()


# Example Output:
# 2023-09-21T01:25:07: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:25:07: %AETEST-INFO: |                            Starting common setup                             |
# 2023-09-21T01:25:07: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:25:07: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:25:07: %AETEST-INFO: |                        Starting subsection subsection                        |
# 2023-09-21T01:25:07: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:25:07: %AETEST-ERROR: Errored reason: setup error, abandoning script
# 2023-09-21T01:25:07: %AETEST-INFO: The result of subsection subsection is => ERRORED
# 2023-09-21T01:25:07: %AETEST-INFO: The result of common setup is => ERRORED
# 2023-09-21T01:25:07: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:25:07: %AETEST-INFO: |                        Starting testcase TestcaseOne                         |
# 2023-09-21T01:25:07: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:25:07: %AETEST-WARNING: Goto 'exit': aborting script run immediately.
# 2023-09-21T01:25:07: %AETEST-INFO: The result of testcase TestcaseOne is => ABORTED
# 2023-09-21T01:25:07: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:25:07: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-21T01:25:07: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:25:07: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-21T01:25:07: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-21T01:25:07: %AETEST-INFO: .
# 2023-09-21T01:25:07: %AETEST-INFO: |-- common_setup                                                         ERRORED
# 2023-09-21T01:25:07: %AETEST-INFO: |   `-- subsection                                                       ERRORED
# 2023-09-21T01:25:07: %AETEST-INFO: `-- TestcaseOne                                                          ABORTED
# 2023-09-21T01:25:07: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:25:07: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-21T01:25:07: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:25:07: %AETEST-INFO:  Number of ABORTED                                                            1
# 2023-09-21T01:25:07: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-21T01:25:07: %AETEST-INFO:  Number of ERRORED                                                            1
# 2023-09-21T01:25:07: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-21T01:25:07: %AETEST-INFO:  Number of PASSED                                                             0
# 2023-09-21T01:25:07: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-21T01:25:07: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-21T01:25:07: %AETEST-INFO:  Total Number                                                                 2
# 2023-09-21T01:25:07: %AETEST-INFO:  Success Rate                                                              0.0%
# 2023-09-21T01:25:07: %AETEST-INFO: --------------------------------------------------------------------------------
