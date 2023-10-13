from pyats.easypy import run

# import the logic objects
from pyats.datastructures.logic import And, Not


# create a function that tests for testcase groups
# this api tests that a testcase belongs to sanity but not traffic.
# note that varargs (using *) is required, as the list of groups to each
# testcase is unknown.
def non_traffic_sanities(*groups):
    # Runs testcases in "sanity" group and not in "traffic" group
    return "sanity" in groups and "traffic" not in groups


# Runs the testscript as two tasks using different logic testing
def main(runtime):
    ### Using function testing (callable) to evaluate testcase groups ###
    # Only runs Testcase Two
    run(testscript="example_script.py", runtime=runtime, groups=non_traffic_sanities)

    ### Using logic testing to evaluate testcase groups ###
    # Only runs Testcase One
    run("example_script.py", groups=And("sanity", Not("traffic")))


# Run the job:
# pyats run job specific_testcase_group_job.py --testbed-file ../testbed.yaml

# Example Output (Results section only for brevity):
# You'll notice two Tasks (each running one Testcase) are created for each testscript run using the different evaluation methods
# 2023-09-24T13:51:53: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T13:51:53: %EASYPY-INFO: |                             Task Result Summary                              |
# 2023-09-24T13:51:53: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T13:51:53: %EASYPY-INFO: Task-1: example_script.TestcaseTwo                                        PASSED
# 2023-09-24T13:51:53: %EASYPY-INFO: Task-2: example_script.TestcaseTwo                                        PASSED
# 2023-09-24T13:51:53: %EASYPY-INFO:
# 2023-09-24T13:51:53: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T13:51:53: %EASYPY-INFO: |                             Task Result Details                              |
# 2023-09-24T13:51:53: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T13:51:53: %EASYPY-INFO: Task-1: example_script
# 2023-09-24T13:51:53: %EASYPY-INFO: `-- TestcaseTwo                                                           PASSED
# 2023-09-24T13:51:53: %EASYPY-INFO:     |-- test1                                                             PASSED
# 2023-09-24T13:51:53: %EASYPY-INFO:     |-- test2                                                             PASSED
# 2023-09-24T13:51:53: %EASYPY-INFO:     `-- testcase_cleanup                                                  PASSED
# 2023-09-24T13:51:53: %EASYPY-INFO: Task-2: example_script
# 2023-09-24T13:51:53: %EASYPY-INFO: `-- TestcaseTwo                                                           PASSED
# 2023-09-24T13:51:53: %EASYPY-INFO:     |-- test1                                                             PASSED
# 2023-09-24T13:51:53: %EASYPY-INFO:     |-- test2                                                             PASSED
# 2023-09-24T13:51:53: %EASYPY-INFO:     `-- testcase_cleanup                                                  PASSED
