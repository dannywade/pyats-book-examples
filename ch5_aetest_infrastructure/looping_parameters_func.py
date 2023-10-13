from pyats import aetest


# callable function
def my_function():
    value = [1, 2, 3]
    print("returning %s" % value)
    return value


# generator
def my_generator():
    for i in [4, 5, 6]:
        print("generating %s" % i)
        yield i


class Testcase(aetest.Testcase):
    # creating test section with parameter "a" as a function
    # note that the function object is passed, not its values
    @aetest.test.loop(a=my_function)
    def test_one(self, a):
        print("a = %s" % a)

    # creating a test section with parameter "b" as a generator
    # note that the generator is a result of calling my_generator(), not
    # the function itself.
    @aetest.test.loop(b=my_generator())
    def test_two(self, b):
        print("b = %s" % b)


if __name__ == "__main__":
    aetest.main()


# Example Output:
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO: |                          Starting testcase Testcase                          |
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# returning [1, 2, 3]
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO: |                        Starting section test_one[a=1]                        |
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# a = 1
# 2023-09-21T00:27:47: %AETEST-INFO: The result of section test_one[a=1] is => PASSED
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO: |                        Starting section test_one[a=2]                        |
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# a = 2
# 2023-09-21T00:27:47: %AETEST-INFO: The result of section test_one[a=2] is => PASSED
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO: |                        Starting section test_one[a=3]                        |
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# a = 3
# 2023-09-21T00:27:47: %AETEST-INFO: The result of section test_one[a=3] is => PASSED
# generating 4
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO: |                        Starting section test_two[b=4]                        |
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# b = 4
# 2023-09-21T00:27:47: %AETEST-INFO: The result of section test_two[b=4] is => PASSED
# generating 5
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO: |                        Starting section test_two[b=5]                        |
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# b = 5
# 2023-09-21T00:27:47: %AETEST-INFO: The result of section test_two[b=5] is => PASSED
# generating 6
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO: |                        Starting section test_two[b=6]                        |
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# b = 6
# 2023-09-21T00:27:47: %AETEST-INFO: The result of section test_two[b=6] is => PASSED
# 2023-09-21T00:27:47: %AETEST-INFO: The result of testcase Testcase is => PASSED
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-21T00:27:47: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-21T00:27:47: %AETEST-INFO: .
# 2023-09-21T00:27:47: %AETEST-INFO: `-- Testcase                                                              PASSED
# 2023-09-21T00:27:47: %AETEST-INFO:     |-- test_one[a=1]                                                     PASSED
# 2023-09-21T00:27:47: %AETEST-INFO:     |-- test_one[a=2]                                                     PASSED
# 2023-09-21T00:27:47: %AETEST-INFO:     |-- test_one[a=3]                                                     PASSED
# 2023-09-21T00:27:47: %AETEST-INFO:     |-- test_two[b=4]                                                     PASSED
# 2023-09-21T00:27:47: %AETEST-INFO:     |-- test_two[b=5]                                                     PASSED
# 2023-09-21T00:27:47: %AETEST-INFO:     `-- test_two[b=6]                                                     PASSED
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-21T00:27:47: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:27:47: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-21T00:27:47: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-21T00:27:47: %AETEST-INFO:  Number of ERRORED                                                            0
# 2023-09-21T00:27:47: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-21T00:27:47: %AETEST-INFO:  Number of PASSED                                                             1
# 2023-09-21T00:27:47: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-21T00:27:47: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-21T00:27:47: %AETEST-INFO:  Total Number                                                                 1
# 2023-09-21T00:27:47: %AETEST-INFO:  Success Rate                                                            100.0%
# 2023-09-21T00:27:47: %AETEST-INFO: --------------------------------------------------------------------------------
