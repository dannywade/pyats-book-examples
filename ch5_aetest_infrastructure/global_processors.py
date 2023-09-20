from pyats import aetest 
 
# Print section uid 
def print_uid(section): 
    print("current section: ", section.uid) 
 
# Print section result 
def print_result(section): 
    print("section result: ", section.result) 
 
# Print the exception message and suppress the exception 
def print_exception_message(section, exc_type, exc_value, exc_traceback): 
    print("exception : ", exc_type, exc_value) 
    return True 
 
# Use the above functions to define global pre/post processors 
#   global pre-processor  : print_uid 
#   global post-processor : print_result 
#   global exception-processor : print_exception_message 
global_processors = { 
    "pre": [print_uid,], 
    "post": [print_result,], 
    "exception": [print_exception_message,], 
} 
 
class Testcase(aetest.Testcase): 
 
    @aetest.test 
    def test(self): 
        print("running testcase test section")

if __name__ == "__main__":
    aetest.main()

# You'll notice the different processor print statements in the output

# Example Output:
# 2023-09-20T01:31:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:31:11: %AETEST-INFO: |                          Starting testcase Testcase                          |
# 2023-09-20T01:31:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# current section:  Testcase
# 2023-09-20T01:31:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:31:11: %AETEST-INFO: |                            Starting section test                             |
# 2023-09-20T01:31:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# current section:  test
# running testcase test section
# section result:  passed
# 2023-09-20T01:31:11: %AETEST-INFO: The result of section test is => PASSED
# section result:  passed
# 2023-09-20T01:31:11: %AETEST-INFO: The result of testcase Testcase is => PASSED
# 2023-09-20T01:31:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:31:11: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-20T01:31:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:31:11: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
# 2023-09-20T01:31:11: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-20T01:31:11: %AETEST-INFO: .
# 2023-09-20T01:31:11: %AETEST-INFO: `-- Testcase                                                              PASSED
# 2023-09-20T01:31:11: %AETEST-INFO:     `-- test                                                              PASSED
# 2023-09-20T01:31:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:31:11: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-20T01:31:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:31:11: %AETEST-INFO:  Number of ABORTED                                                            0 
# 2023-09-20T01:31:11: %AETEST-INFO:  Number of BLOCKED                                                            0 
# 2023-09-20T01:31:11: %AETEST-INFO:  Number of ERRORED                                                            0 
# 2023-09-20T01:31:11: %AETEST-INFO:  Number of FAILED                                                             0 
# 2023-09-20T01:31:11: %AETEST-INFO:  Number of PASSED                                                             1 
# 2023-09-20T01:31:11: %AETEST-INFO:  Number of PASSX                                                              0 
# 2023-09-20T01:31:11: %AETEST-INFO:  Number of SKIPPED                                                            0 
# 2023-09-20T01:31:11: %AETEST-INFO:  Total Number                                                                 1 
# 2023-09-20T01:31:11: %AETEST-INFO:  Success Rate                                                            100.0% 
# 2023-09-20T01:31:11: %AETEST-INFO: --------------------------------------------------------------------------------