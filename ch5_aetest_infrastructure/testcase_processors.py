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


# Use the above functions as pre/post/exception processors to a Testcase
#   pre-processor  : print_uid
#   post-processor : print_result
#   exception-processor : print_exception_message
@aetest.processors(
    pre=[print_uid], post=[print_result], exception=[print_exception_message]
)
class Testcase(aetest.Testcase):
    @aetest.test
    def test(self):
        print("First test section...")

    @aetest.test
    def testException(self):
        raise Exception("Exception raised during testing...")


if __name__ == "__main__":
    aetest.main()


# You'll notice in the Example Output that all tests passed even though an exception was raised

# Example Output:
# 2023-09-20T01:27:21: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:27:21: %AETEST-INFO: |                          Starting testcase Testcase                          |
# 2023-09-20T01:27:21: %AETEST-INFO: +------------------------------------------------------------------------------+
# current section:  Testcase
# 2023-09-20T01:27:21: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:27:21: %AETEST-INFO: |                            Starting section test                             |
# 2023-09-20T01:27:21: %AETEST-INFO: +------------------------------------------------------------------------------+
# First test section...
# 2023-09-20T01:27:21: %AETEST-INFO: The result of section test is => PASSED
# 2023-09-20T01:27:21: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:27:21: %AETEST-INFO: |                        Starting section testException                        |
# 2023-09-20T01:27:21: %AETEST-INFO: +------------------------------------------------------------------------------+
# exception :  <class 'Exception'> Exception raised during testing...
# 2023-09-20T01:27:21: %AETEST-ERROR: Suppressed exception:
# 2023-09-20T01:27:21: %AETEST-ERROR: Caught an exception while executing section testException:
# 2023-09-20T01:27:21: %AETEST-ERROR: Traceback (most recent call last):
# 2023-09-20T01:27:21: %AETEST-ERROR:   File "/workspaces/pyats-book-examples/ch5_aetest_infrastructure/testcase_processors.py", line 31, in testException
# 2023-09-20T01:27:21: %AETEST-ERROR:     raise Exception("Exception raised during testing...")
# 2023-09-20T01:27:21: %AETEST-ERROR: Exception: Exception raised during testing...
# 2023-09-20T01:27:21: %AETEST-ERROR:
# 2023-09-20T01:27:21: %AETEST-INFO: The result of section testException is => PASSED
# section result:  passed
# 2023-09-20T01:27:21: %AETEST-INFO: The result of testcase Testcase is => PASSED
# 2023-09-20T01:27:21: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:27:21: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-20T01:27:21: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:27:21: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-20T01:27:21: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-20T01:27:21: %AETEST-INFO: .
# 2023-09-20T01:27:21: %AETEST-INFO: `-- Testcase                                                              PASSED
# 2023-09-20T01:27:21: %AETEST-INFO:     |-- test                                                              PASSED
# 2023-09-20T01:27:21: %AETEST-INFO:     `-- testException                                                     PASSED
# 2023-09-20T01:27:21: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:27:21: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-20T01:27:21: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:27:21: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-20T01:27:21: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-20T01:27:21: %AETEST-INFO:  Number of ERRORED                                                            0
# 2023-09-20T01:27:21: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-20T01:27:21: %AETEST-INFO:  Number of PASSED                                                             1
# 2023-09-20T01:27:21: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-20T01:27:21: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-20T01:27:21: %AETEST-INFO:  Total Number                                                                 1
# 2023-09-20T01:27:21: %AETEST-INFO:  Success Rate                                                            100.0%
# 2023-09-20T01:27:21: %AETEST-INFO: --------------------------------------------------------------------------------
