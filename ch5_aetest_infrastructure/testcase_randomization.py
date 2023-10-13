from pyats import aetest


# define a couple testcases
class TestcaseOne(aetest.Testcase):
    pass


class TestcaseTwo(aetest.Testcase):
    pass


class TestcaseThree(aetest.Testcase):
    pass


if __name__ == "__main__":
    aetest.main(random=True)


# Example Output:
# 2023-09-21T01:29:22: %AETEST-INFO: Testcase randomization is enabled, seed: 1756046473221811152
# 2023-09-21T01:29:22: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:29:22: %AETEST-INFO: |                        Starting testcase TestcaseTwo                         |
# 2023-09-21T01:29:22: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:29:22: %AETEST-INFO: The result of testcase TestcaseTwo is => PASSED
# 2023-09-21T01:29:22: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:29:22: %AETEST-INFO: |                       Starting testcase TestcaseThree                        |
# 2023-09-21T01:29:22: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:29:22: %AETEST-INFO: The result of testcase TestcaseThree is => PASSED
# 2023-09-21T01:29:22: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:29:22: %AETEST-INFO: |                        Starting testcase TestcaseOne                         |
# 2023-09-21T01:29:22: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:29:22: %AETEST-INFO: The result of testcase TestcaseOne is => PASSED
# 2023-09-21T01:29:22: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:29:22: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-21T01:29:22: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:29:22: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-21T01:29:22: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-21T01:29:22: %AETEST-INFO: .
# 2023-09-21T01:29:22: %AETEST-INFO: |-- TestcaseTwo                                                           PASSED
# 2023-09-21T01:29:22: %AETEST-INFO: |-- TestcaseThree                                                         PASSED
# 2023-09-21T01:29:22: %AETEST-INFO: `-- TestcaseOne                                                           PASSED
# 2023-09-21T01:29:22: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:29:22: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-21T01:29:22: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:29:22: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-21T01:29:22: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-21T01:29:22: %AETEST-INFO:  Number of ERRORED                                                            0
# 2023-09-21T01:29:22: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-21T01:29:22: %AETEST-INFO:  Number of PASSED                                                             3
# 2023-09-21T01:29:22: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-21T01:29:22: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-21T01:29:22: %AETEST-INFO:  Total Number                                                                 3
# 2023-09-21T01:29:22: %AETEST-INFO:  Success Rate                                                            100.0%
# 2023-09-21T01:29:22: %AETEST-INFO: --------------------------------------------------------------------------------
