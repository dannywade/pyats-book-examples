from pyats import aetest


class ResultTestcase(aetest.Testcase):
    @aetest.test
    def subsection_that_passes(self):
        self.passed("This test passed!")

    @aetest.test
    def subsection_that_skips(self):
        self.skipped("This test skipped!")

    @aetest.test
    def subsection_that_is_errored(self):
        self.errored("This test errored!")


if __name__ == "__main__":
    aetest.main()

# Example Output:
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO: |                       Starting testcase ResultTestcase                       |
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO: |                   Starting section subsection_that_passes                    |
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO: Passed reason: This test passed!
# 2023-09-20T01:24:51: %AETEST-INFO: The result of section subsection_that_passes is => PASSED
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO: |                    Starting section subsection_that_skips                    |
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO: Skipped reason: This test skipped!
# 2023-09-20T01:24:51: %AETEST-INFO: The result of section subsection_that_skips is => SKIPPED
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO: |                 Starting section subsection_that_is_errored                  |
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-ERROR: Errored reason: This test errored!
# 2023-09-20T01:24:51: %AETEST-INFO: The result of section subsection_that_is_errored is => ERRORED
# 2023-09-20T01:24:51: %AETEST-INFO: The result of testcase ResultTestcase is => ERRORED
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-20T01:24:51: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-20T01:24:51: %AETEST-INFO: .
# 2023-09-20T01:24:51: %AETEST-INFO: `-- ResultTestcase                                                       ERRORED
# 2023-09-20T01:24:51: %AETEST-INFO:     |-- subsection_that_passes                                            PASSED
# 2023-09-20T01:24:51: %AETEST-INFO:     |-- subsection_that_skips                                            SKIPPED
# 2023-09-20T01:24:51: %AETEST-INFO:     `-- subsection_that_is_errored                                       ERRORED
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-20T01:24:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:24:51: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-20T01:24:51: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-20T01:24:51: %AETEST-INFO:  Number of ERRORED                                                            1
# 2023-09-20T01:24:51: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-20T01:24:51: %AETEST-INFO:  Number of PASSED                                                             0
# 2023-09-20T01:24:51: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-20T01:24:51: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-20T01:24:51: %AETEST-INFO:  Total Number                                                                 1
# 2023-09-20T01:24:51: %AETEST-INFO:  Success Rate                                                              0.0%
# 2023-09-20T01:24:51: %AETEST-INFO: --------------------------------------------------------------------------------
