from pyats import aetest 

class MyCommonSetup(aetest.CommonSetup):
    """Common Setup"""

    @aetest.subsection 
    def connect_to_devices(self): 
        """Code to connect to testbed devices"""
        pass 


    @aetest.subsection 
    def apply_base_config(self): 
        """Code to configure devices with base/initial config"""
        pass

if __name__ == "__main__":
    aetest.main()

# Example Output:
# 2023-09-20T01:02:20: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:02:20: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-20T01:02:20: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:02:20: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
# 2023-09-20T01:02:20: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-20T01:02:20: %AETEST-INFO: .
# 2023-09-20T01:02:20: %AETEST-INFO: `-- common_setup                                                          PASSED
# 2023-09-20T01:02:20: %AETEST-INFO:     |-- connect_to_devices                                                PASSED
# 2023-09-20T01:02:20: %AETEST-INFO:     `-- apply_base_config                                                 PASSED
# 2023-09-20T01:02:20: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:02:20: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-20T01:02:20: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:02:20: %AETEST-INFO:  Number of ABORTED                                                            0 
# 2023-09-20T01:02:20: %AETEST-INFO:  Number of BLOCKED                                                            0 
# 2023-09-20T01:02:20: %AETEST-INFO:  Number of ERRORED                                                            0 
# 2023-09-20T01:02:20: %AETEST-INFO:  Number of FAILED                                                             0 
# 2023-09-20T01:02:20: %AETEST-INFO:  Number of PASSED                                                             1 
# 2023-09-20T01:02:20: %AETEST-INFO:  Number of PASSX                                                              0 
# 2023-09-20T01:02:20: %AETEST-INFO:  Number of SKIPPED                                                            0 
# 2023-09-20T01:02:20: %AETEST-INFO:  Total Number                                                                 1 
# 2023-09-20T01:02:20: %AETEST-INFO:  Success Rate                                                            100.0% 
# 2023-09-20T01:02:20: %AETEST-INFO: --------------------------------------------------------------------------------