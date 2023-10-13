from pyats import aetest

# Script-level parameters
parameters = {
    "param_A": 1,
    "param_B": dict(),
}


class Testcase(aetest.Testcase):
    # "param_B” is passed to the setup section as a function argument
    @aetest.setup
    def setup(self, param_B):
        # param_B is a dictionary and can be changed (mutable)
        # Any changes are persist throughout the testscript
        param_B["new_key"] = "a key added during setup section"

    # "param_A" and "param_B" are passed to the test section
    @aetest.test
    def test_one(self, param_A, param_B):
        print(param_A)
        # 1
        print(param_B)
        # {"new_key": 'a key added during setup section'}


if __name__ == "__main__":
    aetest.main()


# Example Output:
# 2023-09-20T01:42:59: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:42:59: %AETEST-INFO: |                          Starting testcase Testcase                          |
# 2023-09-20T01:42:59: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:42:59: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:42:59: %AETEST-INFO: |                            Starting section setup                            |
# 2023-09-20T01:42:59: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:42:59: %AETEST-INFO: The result of section setup is => PASSED
# 2023-09-20T01:42:59: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:42:59: %AETEST-INFO: |                          Starting section test_one                           |
# 2023-09-20T01:42:59: %AETEST-INFO: +------------------------------------------------------------------------------+
# 1
# {'new_key': 'a key added during setup section'}
# 2023-09-20T01:42:59: %AETEST-INFO: The result of section test_one is => PASSED
# 2023-09-20T01:42:59: %AETEST-INFO: The result of testcase Testcase is => PASSED
# 2023-09-20T01:42:59: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:42:59: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-20T01:42:59: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:42:59: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-20T01:42:59: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-20T01:42:59: %AETEST-INFO: .
# 2023-09-20T01:42:59: %AETEST-INFO: `-- Testcase                                                              PASSED
# 2023-09-20T01:42:59: %AETEST-INFO:     |-- setup                                                             PASSED
# 2023-09-20T01:42:59: %AETEST-INFO:     `-- test_one                                                          PASSED
# 2023-09-20T01:42:59: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:42:59: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-20T01:42:59: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:42:59: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-20T01:42:59: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-20T01:42:59: %AETEST-INFO:  Number of ERRORED                                                            0
# 2023-09-20T01:42:59: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-20T01:42:59: %AETEST-INFO:  Number of PASSED                                                             1
# 2023-09-20T01:42:59: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-20T01:42:59: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-20T01:42:59: %AETEST-INFO:  Total Number                                                                 1
# 2023-09-20T01:42:59: %AETEST-INFO:  Success Rate                                                            100.0%
# 2023-09-20T01:42:59: %AETEST-INFO: --------------------------------------------------------------------------------
