from pyats import aetest


class Testcase(aetest.Testcase):
    @aetest.test
    def test(self, steps):
        # demonstrating a step with multiple child steps
        with steps.start("test step 1") as step:
            with step.start("test step 1 substep a"):
                pass
            with step.start("test step 1 substep a") as substep:
                with substep.start("test step 1 sub-step a sub-substep i"):
                    pass
                with substep.start("test step 1 sub-step a sub-substep ii"):
                    pass


if __name__ == "__main__":
    aetest.main()

# Example Output:
# 2023-09-20T01:00:11: %AETEST-INFO: +..........................................................+
# 2023-09-20T01:00:11: %AETEST-INFO: :                       STEPS Report                       :
# 2023-09-20T01:00:11: %AETEST-INFO: +..........................................................+
# 2023-09-20T01:00:11: %AETEST-INFO: STEP 1 - test step 1                              Passed
# 2023-09-20T01:00:11: %AETEST-INFO: STEP 1.1 - test step 1 substep a                  Passed
# 2023-09-20T01:00:11: %AETEST-INFO: STEP 1.2 - test step 1 substep a                  Passed
# 2023-09-20T01:00:11: %AETEST-INFO: STEP 1.2.1 - test step 1 sub-step a sub-substep i Passed
# 2023-09-20T01:00:11: %AETEST-INFO: STEP 1.2.2 - test step 1 sub-step a sub-substep iiPassed
# 2023-09-20T01:00:11: %AETEST-INFO: ............................................................
# 2023-09-20T01:00:11: %AETEST-INFO: The result of section test is => PASSED
# 2023-09-20T01:00:11: %AETEST-INFO: The result of testcase Testcase is => PASSED
# 2023-09-20T01:00:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:00:11: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-20T01:00:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:00:11: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-20T01:00:11: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-20T01:00:11: %AETEST-INFO: .
# 2023-09-20T01:00:11: %AETEST-INFO: `-- Testcase                                                              PASSED
# 2023-09-20T01:00:11: %AETEST-INFO:     `-- test                                                              PASSED
# 2023-09-20T01:00:11: %AETEST-INFO:         |-- Step 1: test step 1                                           PASSED
# 2023-09-20T01:00:11: %AETEST-INFO:         |-- Step 1.1: test step 1 substep a                               PASSED
# 2023-09-20T01:00:11: %AETEST-INFO:         |-- Step 1.2: test step 1 substep a                               PASSED
# 2023-09-20T01:00:11: %AETEST-INFO:         |-- Step 1.2.1: test step 1 sub-step a sub-substep i              PASSED
# 2023-09-20T01:00:11: %AETEST-INFO:         `-- Step 1.2.2: test step 1 sub-step a sub-substep ii             PASSED
# 2023-09-20T01:00:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:00:11: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-20T01:00:11: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-20T01:00:11: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-20T01:00:11: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-20T01:00:11: %AETEST-INFO:  Number of ERRORED                                                            0
# 2023-09-20T01:00:11: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-20T01:00:11: %AETEST-INFO:  Number of PASSED                                                             1
# 2023-09-20T01:00:11: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-20T01:00:11: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-20T01:00:11: %AETEST-INFO:  Total Number                                                                 1
# 2023-09-20T01:00:11: %AETEST-INFO:  Success Rate                                                            100.0%
# 2023-09-20T01:00:11: %AETEST-INFO: --------------------------------------------------------------------------------
