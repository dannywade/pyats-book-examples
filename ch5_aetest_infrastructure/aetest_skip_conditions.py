from pyats import aetest 

# Custom library used for testing
class mylibrary:
    __version__ = 0.1

# skip testcase intentionally 
@aetest.skip('because we had to') 
class Testcase(aetest.Testcase): 
    pass 
 
class TestcaseTwo(aetest.Testcase): 
 
    # skip test section using if library version < some number 
    @aetest.skipIf(mylibrary.__version__ < 1, 'not supported in this library version') 
    @aetest.test 
    def test_one(self): 
        pass 
 
    # skip unless library version > some number 
    @aetest.skipUnless(mylibrary.__version__ > 3, 'not supported in this library version') 
    @aetest.test 
    def test_two(self): 
        pass 
 
    @aetest.test 
    def test_three(self): 
        aetest.skip.affix(section = TestcaseTwo.test_four, 
                          reason = "message") 
        aetest.skipIf.affix(section = TestcaseTwo.test_five, 
                            condition = True, 
                            reason = "message") 
        aetest.skipUnless.affix(section = TestcaseThree, 
                                condition = False, 
                                reason = "message") 
 
    @aetest.test 
    def test_four(self): 
        # will be skipped because of test_three 
        pass 
 
    @aetest.test 
    def test_five(self): 
        # will be skipped because of test_three 
        pass 
 
    @aetest.test 
    def test_six(self): 
        # will be skipped because of test_three 
        pass 
 
class TestcaseThree(aetest.Testcase): 
    # will be skipped because of TestcaseTwo.test_three 
    pass 

if __name__ == "__main__":
    aetest.main()


# Example Output:
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                          Starting testcase Testcase                          |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: Skipped reason: PreProcessor-1 'skip' - because we had to
# 2023-09-21T01:09:53: %AETEST-INFO: The result of testcase Testcase is => SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                        Starting testcase TestcaseTwo                         |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                          Starting section test_one                           |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: Skipped reason: PreProcessor-1 'skipIf' - not supported in this library version
# 2023-09-21T01:09:53: %AETEST-INFO: The result of section test_one is => SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                          Starting section test_two                           |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: Skipped reason: PreProcessor-1 'skipUnless' - not supported in this library version
# 2023-09-21T01:09:53: %AETEST-INFO: The result of section test_two is => SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                         Starting section test_three                          |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: The result of section test_three is => PASSED
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                          Starting section test_four                          |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: Skipped reason: PreProcessor-1 'skip' - message
# 2023-09-21T01:09:53: %AETEST-INFO: The result of section test_four is => SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                          Starting section test_five                          |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: Skipped reason: PreProcessor-1 'skipIf' - message
# 2023-09-21T01:09:53: %AETEST-INFO: The result of section test_five is => SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                          Starting section test_six                           |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: The result of section test_six is => PASSED
# 2023-09-21T01:09:53: %AETEST-INFO: The result of testcase TestcaseTwo is => PASSED
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                       Starting testcase TestcaseThree                        |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: Skipped reason: PreProcessor-1 'skipUnless' - message
# 2023-09-21T01:09:53: %AETEST-INFO: The result of testcase TestcaseThree is => SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT   
# 2023-09-21T01:09:53: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-21T01:09:53: %AETEST-INFO: .
# 2023-09-21T01:09:53: %AETEST-INFO: |-- Testcase                                                             SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: |-- TestcaseTwo                                                           PASSED
# 2023-09-21T01:09:53: %AETEST-INFO: |   |-- test_one                                                         SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: |   |-- test_two                                                         SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: |   |-- test_three                                                        PASSED
# 2023-09-21T01:09:53: %AETEST-INFO: |   |-- test_four                                                        SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: |   |-- test_five                                                        SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: |   `-- test_six                                                          PASSED
# 2023-09-21T01:09:53: %AETEST-INFO: `-- TestcaseThree                                                        SKIPPED
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-21T01:09:53: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T01:09:53: %AETEST-INFO:  Number of ABORTED                                                            0 
# 2023-09-21T01:09:53: %AETEST-INFO:  Number of BLOCKED                                                            0 
# 2023-09-21T01:09:53: %AETEST-INFO:  Number of ERRORED                                                            0 
# 2023-09-21T01:09:53: %AETEST-INFO:  Number of FAILED                                                             0 
# 2023-09-21T01:09:53: %AETEST-INFO:  Number of PASSED                                                             1 
# 2023-09-21T01:09:53: %AETEST-INFO:  Number of PASSX                                                              0 
# 2023-09-21T01:09:53: %AETEST-INFO:  Number of SKIPPED                                                            2 
# 2023-09-21T01:09:53: %AETEST-INFO:  Total Number                                                                 3 
# 2023-09-21T01:09:53: %AETEST-INFO:  Success Rate                                                            100.0% 
# 2023-09-21T01:09:53: %AETEST-INFO: --------------------------------------------------------------------------------