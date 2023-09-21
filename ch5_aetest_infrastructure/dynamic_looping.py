from pyats import aetest 
 
class Testcase(aetest.Testcase): 
 
    @aetest.setup 
    def setup(self): 
        # mark the next test for looping 
        # provide it with two unique test uids. 
        # (self.simple_test is the next test method) 
        aetest.loop.mark(self.simple_test, uids=["test_one", "test_two"]) 
 
    # note: the simple_test section is not directly marked for looping 
    # instead, during runtime, its testcase's setup section marks it for 
    # looping dynamically. 
 
    @aetest.test 
    def simple_test(self, section): 
        # print the current section uid 
        # by using the internal parameter "section" 
        print("current section: %s" % section.uid) 

if __name__ == "__main__":
    aetest.main()


# Example Output:
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:30:08: %AETEST-INFO: |                          Starting testcase Testcase                          |
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:30:08: %AETEST-INFO: |                            Starting section setup                            |
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:30:08: %AETEST-INFO: The result of section setup is => PASSED
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:30:08: %AETEST-INFO: |                          Starting section test_one                           |
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# current section: test_one
# 2023-09-21T00:30:08: %AETEST-INFO: The result of section test_one is => PASSED
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:30:08: %AETEST-INFO: |                          Starting section test_two                           |
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# current section: test_two
# 2023-09-21T00:30:08: %AETEST-INFO: The result of section test_two is => PASSED
# 2023-09-21T00:30:08: %AETEST-INFO: The result of testcase Testcase is => PASSED
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:30:08: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:30:08: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
# 2023-09-21T00:30:08: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-21T00:30:08: %AETEST-INFO: .
# 2023-09-21T00:30:08: %AETEST-INFO: `-- Testcase                                                              PASSED
# 2023-09-21T00:30:08: %AETEST-INFO:     |-- setup                                                             PASSED
# 2023-09-21T00:30:08: %AETEST-INFO:     |-- test_one                                                          PASSED
# 2023-09-21T00:30:08: %AETEST-INFO:     `-- test_two                                                          PASSED
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:30:08: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-21T00:30:08: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:30:08: %AETEST-INFO:  Number of ABORTED                                                            0 
# 2023-09-21T00:30:08: %AETEST-INFO:  Number of BLOCKED                                                            0 
# 2023-09-21T00:30:08: %AETEST-INFO:  Number of ERRORED                                                            0 
# 2023-09-21T00:30:08: %AETEST-INFO:  Number of FAILED                                                             0 
# 2023-09-21T00:30:08: %AETEST-INFO:  Number of PASSED                                                             1 
# 2023-09-21T00:30:08: %AETEST-INFO:  Number of PASSX                                                              0 
# 2023-09-21T00:30:08: %AETEST-INFO:  Number of SKIPPED                                                            0 
# 2023-09-21T00:30:08: %AETEST-INFO:  Total Number                                                                 1 
# 2023-09-21T00:30:08: %AETEST-INFO:  Success Rate                                                            100.0% 
# 2023-09-21T00:30:08: %AETEST-INFO: --------------------------------------------------------------------------------