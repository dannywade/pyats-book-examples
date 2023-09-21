from pyats import aetest 
 
 
class TestcaseOne(aetest.Testcase): 
 
    must_pass = True 
 
    @aetest.test 
    def test(self): 
        self.failed('boom!') 
 
class TestcaseTwo(aetest.Testcase): 
    pass 
 
class CommonCleanup(aetest.CommonCleanup):
 
    @aetest.subsection 
    def subsection(self): 
        pass 

if __name__ == "__main__":
    aetest.main()


# Example Output:
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: |                        Starting testcase TestcaseOne                         |
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: |                            Starting section test                             |
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-ERROR: Failed reason: boom!
# 2023-09-21T01:27:04: %AETEST-INFO: The result of section test is => FAILED
# 2023-09-21T01:27:04: %AETEST-ERROR: Testcase marked must-pass: aborting script execution
# 2023-09-21T01:27:04: %AETEST-INFO: The result of testcase TestcaseOne is => FAILED
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: |                        Starting testcase TestcaseTwo                         |
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: Skipping/blocking due to goto: common_cleanup
# 2023-09-21T01:27:04: %AETEST-INFO: The result of testcase TestcaseTwo is => BLOCKED
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: |                           Starting common cleanup                            |
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: |                        Starting subsection subsection                        |
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: The result of subsection subsection is => PASSED
# 2023-09-21T01:27:04: %AETEST-INFO: The result of common cleanup is => PASSED
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
# 2023-09-21T01:27:04: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-21T01:27:04: %AETEST-INFO: .
# 2023-09-21T01:27:04: %AETEST-INFO: |-- TestcaseOne                                                           FAILED
# 2023-09-21T01:27:04: %AETEST-INFO: |   `-- test                                                              FAILED
# 2023-09-21T01:27:04: %AETEST-INFO: |-- TestcaseTwo                                                          BLOCKED
# 2023-09-21T01:27:04: %AETEST-INFO: `-- common_cleanup                                                        PASSED
# 2023-09-21T01:27:04: %AETEST-INFO:     `-- subsection                                                        PASSED
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-21T01:27:04: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:27:04: %AETEST-INFO:  Number of ABORTED                                                            0 
# 2023-09-21T01:27:04: %AETEST-INFO:  Number of BLOCKED                                                            1 
# 2023-09-21T01:27:04: %AETEST-INFO:  Number of ERRORED                                                            0 
# 2023-09-21T01:27:04: %AETEST-INFO:  Number of FAILED                                                             1 
# 2023-09-21T01:27:04: %AETEST-INFO:  Number of PASSED                                                             1 
# 2023-09-21T01:27:04: %AETEST-INFO:  Number of PASSX                                                              0 
# 2023-09-21T01:27:04: %AETEST-INFO:  Number of SKIPPED                                                            0 
# 2023-09-21T01:27:04: %AETEST-INFO:  Total Number                                                                 3 
# 2023-09-21T01:27:04: %AETEST-INFO:  Success Rate                                                             33.3% 
# 2023-09-21T01:27:04: %AETEST-INFO: --------------------------------------------------------------------------------