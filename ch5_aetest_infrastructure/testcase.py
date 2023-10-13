from pyats import aetest


class MyTestcase(aetest.Testcase):
    """Testcase"""

    @aetest.setup
    def testcase_setup(self):
        """Code to setup testbed devices for testcase"""
        pass

    @aetest.test
    def test1(self):
        """Code for first test"""
        pass

    @aetest.test
    def test2(self):
        """Code for second test"""
        pass

    @aetest.cleanup
    def testcase_cleanup(self):
        """Code to cleanup config on testbed devices"""
        pass


if __name__ == "__main__":
    aetest.main()

# Example Output:
# 2023-09-20T01:01:39: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:01:39: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-20T01:01:39: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:01:39: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-20T01:01:39: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-20T01:01:39: %AETEST-INFO: .
# 2023-09-20T01:01:39: %AETEST-INFO: `-- MyTestcase                                                            PASSED
# 2023-09-20T01:01:39: %AETEST-INFO:     |-- testcase_setup                                                    PASSED
# 2023-09-20T01:01:39: %AETEST-INFO:     |-- test1                                                             PASSED
# 2023-09-20T01:01:39: %AETEST-INFO:     |-- test2                                                             PASSED
# 2023-09-20T01:01:39: %AETEST-INFO:     `-- testcase_cleanup                                                  PASSED
# 2023-09-20T01:01:39: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:01:39: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-20T01:01:39: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:01:39: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-20T01:01:39: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-20T01:01:39: %AETEST-INFO:  Number of ERRORED                                                            0
# 2023-09-20T01:01:39: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-20T01:01:39: %AETEST-INFO:  Number of PASSED                                                             1
# 2023-09-20T01:01:39: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-20T01:01:39: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-20T01:01:39: %AETEST-INFO:  Total Number                                                                 1
# 2023-09-20T01:01:39: %AETEST-INFO:  Success Rate                                                            100.0%
# 2023-09-20T01:01:39: %AETEST-INFO: --------------------------------------------------------------------------------
