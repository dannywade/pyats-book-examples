from pyats.easypy import run


# function determining whether we should run testcase_A
# currently executing uids is always a list of:
#       [ <container uid>, <section uid>]
# eg, ['common_setup', 'subsection_one']
# thus varargs (using *) is required for the function input.
def run_only_testcase_one(*uids):
    # check that we are running TestcaseOne
    return "TestcaseOne" in uids


# run only TestcaseOne and its contents (using callable)
# executing uids has TestcaseOne:
def main():
    run("example_script.py", uids=run_only_testcase_one)


# Run the job:
# pyats run job specific_testcase_uid_job.py --testbed-file ../testbed.yaml

# Example Output (Results section only for brevity):
# 2023-09-24T13:30:20: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T13:30:20: %EASYPY-INFO: |                             Task Result Summary                              |
# 2023-09-24T13:30:20: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T13:30:20: %EASYPY-INFO: Task-1: example_script.TestcaseOne                                        PASSED
# 2023-09-24T13:30:20: %EASYPY-INFO:
# 2023-09-24T13:30:20: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T13:30:20: %EASYPY-INFO: |                             Task Result Details                              |
# 2023-09-24T13:30:20: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-09-24T13:30:20: %EASYPY-INFO: Task-1: example_script
# 2023-09-24T13:30:20: %EASYPY-INFO: `-- TestcaseOne                                                           PASSED
# 2023-09-24T13:30:20: %EASYPY-INFO:     |-- test1                                                             PASSED
# 2023-09-24T13:30:20: %EASYPY-INFO:     |-- test2                                                             PASSED
# 2023-09-24T13:30:20: %EASYPY-INFO:     `-- testcase_cleanup                                                  PASSED
