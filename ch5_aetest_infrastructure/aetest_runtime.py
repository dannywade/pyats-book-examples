from pyats import aetest 

from pyats.datastructures.logic import And, Not 
 
class CommonSetup(aetest.CommonSetup): 
 
    # Allows testcases in “L3” and not in “L2” group to execute 
    @aetest.subsection 
    def validate_l3_testcases(self): 
        aetest.runtime.groups = And("L3", Not("L2"))
        # Print runtime groups
        print(aetest.runtime.groups)

if __name__ == "__main__":
    aetest.main()

# Example Output:
# 2023-09-20T01:11:52: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:11:52: %AETEST-INFO: |                            Starting common setup                             |
# 2023-09-20T01:11:52: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:11:52: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:11:52: %AETEST-INFO: |                  Starting subsection validate_l3_testcases                   |
# 2023-09-20T01:11:52: %AETEST-INFO: +------------------------------------------------------------------------------+
# And('L3', Not('L2'))
# 2023-09-20T01:11:52: %AETEST-INFO: The result of subsection validate_l3_testcases is => PASSED
# 2023-09-20T01:11:52: %AETEST-INFO: The result of common setup is => PASSED
# 2023-09-20T01:11:52: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:11:52: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-20T01:11:52: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:11:52: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
# 2023-09-20T01:11:52: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-20T01:11:52: %AETEST-INFO: .
# 2023-09-20T01:11:52: %AETEST-INFO: `-- common_setup                                                          PASSED
# 2023-09-20T01:11:52: %AETEST-INFO:     `-- validate_l3_testcases                                             PASSED
# 2023-09-20T01:11:52: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:11:52: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-20T01:11:52: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:11:52: %AETEST-INFO:  Number of ABORTED                                                            0 
# 2023-09-20T01:11:52: %AETEST-INFO:  Number of BLOCKED                                                            0 
# 2023-09-20T01:11:52: %AETEST-INFO:  Number of ERRORED                                                            0 
# 2023-09-20T01:11:52: %AETEST-INFO:  Number of FAILED                                                             0 
# 2023-09-20T01:11:52: %AETEST-INFO:  Number of PASSED                                                             1 
# 2023-09-20T01:11:52: %AETEST-INFO:  Number of PASSX                                                              0 
# 2023-09-20T01:11:52: %AETEST-INFO:  Number of SKIPPED                                                            0 
# 2023-09-20T01:11:52: %AETEST-INFO:  Total Number                                                                 1 
# 2023-09-20T01:11:52: %AETEST-INFO:  Success Rate                                                            100.0% 
# 2023-09-20T01:11:52: %AETEST-INFO: --------------------------------------------------------------------------------