from pyats.easypy import run 
 
# function determining whether we should run testcase_A 
# currently executing uids is always a list of: 
#       [ <container uid>, <section uid>] 
# eg, ['common_setup', 'subsection_one'] 
# thus varargs (using *) is required for the function input. 
def run_only_testcase_A(*ids): 
    # check that we are running testcase_A 
    return 'testcase_A' in uids 
 
# run only testcase_A and its contents (using callable) 
# executing uids has testcase_A: 
run('example_script.py', uids = run_only_testcase_A) 