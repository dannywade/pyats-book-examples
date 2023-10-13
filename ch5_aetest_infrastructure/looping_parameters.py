from pyats import aetest


class Testcase(aetest.Testcase):
    # Method 1 – args and argvs – the positions of each value match to its arg name
    @aetest.test.loop(args=("a", "b", "c"), argvs=((1, 2, 3), (4, 5, 6)))
    def test_one(self, a, b, c):
        print("a=%s, b=%s, c=%s" % (a, b, c))

    # Method 2 – keyword args – each argument in the lists are provided independently
    @aetest.test.loop(a=[1, 4], b=[2, 5], c=[3, 6])
    def test_two(self, a, b, c):
        print("a=%s, b=%s, c=%s" % (a, b, c))


if __name__ == "__main__":
    aetest.main()

# Example Output:
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:24:42: %AETEST-INFO: |                          Starting testcase Testcase                          |
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:24:42: %AETEST-INFO: |                    Starting section test_one[a=1,b=2,c=3]                    |
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# a=1, b=2, c=3
# 2023-09-21T00:24:42: %AETEST-INFO: The result of section test_one[a=1,b=2,c=3] is => PASSED
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:24:42: %AETEST-INFO: |                    Starting section test_one[a=4,b=5,c=6]                    |
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# a=4, b=5, c=6
# 2023-09-21T00:24:42: %AETEST-INFO: The result of section test_one[a=4,b=5,c=6] is => PASSED
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:24:42: %AETEST-INFO: |                    Starting section test_two[a=1,b=2,c=3]                    |
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# a=1, b=2, c=3
# 2023-09-21T00:24:42: %AETEST-INFO: The result of section test_two[a=1,b=2,c=3] is => PASSED
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:24:42: %AETEST-INFO: |                    Starting section test_two[a=4,b=5,c=6]                    |
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# a=4, b=5, c=6
# 2023-09-21T00:24:42: %AETEST-INFO: The result of section test_two[a=4,b=5,c=6] is => PASSED
# 2023-09-21T00:24:42: %AETEST-INFO: The result of testcase Testcase is => PASSED
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:24:42: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:24:42: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-21T00:24:42: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-21T00:24:42: %AETEST-INFO: .
# 2023-09-21T00:24:42: %AETEST-INFO: `-- Testcase                                                              PASSED
# 2023-09-21T00:24:42: %AETEST-INFO:     |-- test_one[a=1,b=2,c=3]                                             PASSED
# 2023-09-21T00:24:42: %AETEST-INFO:     |-- test_one[a=4,b=5,c=6]                                             PASSED
# 2023-09-21T00:24:42: %AETEST-INFO:     |-- test_two[a=1,b=2,c=3]                                             PASSED
# 2023-09-21T00:24:42: %AETEST-INFO:     `-- test_two[a=4,b=5,c=6]                                             PASSED
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:24:42: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-21T00:24:42: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:24:42: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-21T00:24:42: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-21T00:24:42: %AETEST-INFO:  Number of ERRORED                                                            0
# 2023-09-21T00:24:42: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-21T00:24:42: %AETEST-INFO:  Number of PASSED                                                             1
# 2023-09-21T00:24:42: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-21T00:24:42: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-21T00:24:42: %AETEST-INFO:  Total Number                                                                 1
# 2023-09-21T00:24:42: %AETEST-INFO:  Success Rate                                                            100.0%
# 2023-09-21T00:24:42: %AETEST-INFO: --------------------------------------------------------------------------------
