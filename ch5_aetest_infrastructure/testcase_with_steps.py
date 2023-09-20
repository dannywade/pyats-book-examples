from pyats import aetest 
 
class Testcase(aetest.Testcase): 
    """Testcase with steps"""

    @aetest.test 
    def test(self, steps):
        """Code for test section and steps"""
        # steps.start() begins the step 
        with steps.start("The first step") as step:
            print("This is step one!") 
 
        with steps.start("The second step") as step:
            print("This is step two!")

if __name__ == "__main__":
    aetest.main()

# Example Output:
# 2023-09-20T01:00:51: %AETEST-INFO: +..........................................................+
# 2023-09-20T01:00:51: %AETEST-INFO: :                       STEPS Report                       :
# 2023-09-20T01:00:51: %AETEST-INFO: +..........................................................+
# 2023-09-20T01:00:51: %AETEST-INFO: STEP 1 - The first step                           Passed    
# 2023-09-20T01:00:51: %AETEST-INFO: STEP 2 - The second step                          Passed    
# 2023-09-20T01:00:51: %AETEST-INFO: ............................................................
# 2023-09-20T01:00:51: %AETEST-INFO: The result of section test is => PASSED
# 2023-09-20T01:00:51: %AETEST-INFO: The result of testcase Testcase is => PASSED
# 2023-09-20T01:00:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:00:51: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-20T01:00:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:00:51: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
# 2023-09-20T01:00:51: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-20T01:00:51: %AETEST-INFO: .
# 2023-09-20T01:00:51: %AETEST-INFO: `-- Testcase                                                              PASSED
# 2023-09-20T01:00:51: %AETEST-INFO:     `-- test                                                              PASSED
# 2023-09-20T01:00:51: %AETEST-INFO:         |-- Step 1: The first step                                        PASSED
# 2023-09-20T01:00:51: %AETEST-INFO:         `-- Step 2: The second step                                       PASSED
# 2023-09-20T01:00:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:00:51: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-20T01:00:51: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:00:51: %AETEST-INFO:  Number of ABORTED                                                            0 
# 2023-09-20T01:00:51: %AETEST-INFO:  Number of BLOCKED                                                            0 
# 2023-09-20T01:00:51: %AETEST-INFO:  Number of ERRORED                                                            0 
# 2023-09-20T01:00:51: %AETEST-INFO:  Number of FAILED                                                             0 
# 2023-09-20T01:00:51: %AETEST-INFO:  Number of PASSED                                                             1 
# 2023-09-20T01:00:51: %AETEST-INFO:  Number of PASSX                                                              0 
# 2023-09-20T01:00:51: %AETEST-INFO:  Number of SKIPPED                                                            0 
# 2023-09-20T01:00:51: %AETEST-INFO:  Total Number                                                                 1 
# 2023-09-20T01:00:51: %AETEST-INFO:  Success Rate                                                            100.0% 
# 2023-09-20T01:00:51: %AETEST-INFO: --------------------------------------------------------------------------------