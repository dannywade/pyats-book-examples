from pyats import aetest


class TestcaseOne(aetest.Testcase):
    @aetest.test
    def test(self):
        self.failed()


class TestcaseTwo(aetest.Testcase):
    @aetest.test
    def test(self):
        self.failed()


class TestcaseThree(aetest.Testcase):
    pass


class CommonCleanup(aetest.CommonCleanup):
    pass


# set max failure to 1 and run the testscript
if __name__ == "__main__":
    aetest.main(max_failures=1)


# Example Output:
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: |                        Starting testcase TestcaseOne                         |
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: |                            Starting section test                             |
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: The result of section test is => FAILED
# 2023-09-21T01:31:53: %AETEST-ERROR: Max failure reached: aborting script execution
# 2023-09-21T01:31:53: %AETEST-INFO: The result of testcase TestcaseOne is => FAILED
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: |                        Starting testcase TestcaseTwo                         |
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: Skipping/blocking due to goto: common_cleanup
# 2023-09-21T01:31:53: %AETEST-INFO: The result of testcase TestcaseTwo is => BLOCKED
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: |                       Starting testcase TestcaseThree                        |
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: Skipping/blocking due to goto: common_cleanup
# 2023-09-21T01:31:53: %AETEST-INFO: The result of testcase TestcaseThree is => BLOCKED
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: |                           Starting common cleanup                            |
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: The result of common cleanup is => PASSED
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-21T01:31:53: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-21T01:31:53: %AETEST-INFO: .
# 2023-09-21T01:31:53: %AETEST-INFO: |-- TestcaseOne                                                           FAILED
# 2023-09-21T01:31:53: %AETEST-INFO: |   `-- test                                                              FAILED
# 2023-09-21T01:31:53: %AETEST-INFO: |-- TestcaseTwo                                                          BLOCKED
# 2023-09-21T01:31:53: %AETEST-INFO: |-- TestcaseThree                                                        BLOCKED
# 2023-09-21T01:31:53: %AETEST-INFO: `-- common_cleanup                                                        PASSED
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-21T01:31:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:31:53: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-21T01:31:53: %AETEST-INFO:  Number of BLOCKED                                                            2
# 2023-09-21T01:31:53: %AETEST-INFO:  Number of ERRORED                                                            0
# 2023-09-21T01:31:53: %AETEST-INFO:  Number of FAILED                                                             1
# 2023-09-21T01:31:53: %AETEST-INFO:  Number of PASSED                                                             1
# 2023-09-21T01:31:53: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-21T01:31:53: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-21T01:31:53: %AETEST-INFO:  Total Number                                                                 4
# 2023-09-21T01:31:53: %AETEST-INFO:  Success Rate                                                             25.0%
# 2023-09-21T01:31:53: %AETEST-INFO: --------------------------------------------------------------------------------
