from pyats.easypy import run


# create a function that tests for testcase groups
# this api tests that a testcase belongs to sanity but not traffic.
# note that varargs (using *) is required, as the list of groups to each
# testcase is unknown.
def non_traffic_sanities(*groups):
    return "sanity" in groups and "traffic" not in groups


# run the testscript by providing the above function to test groups
def main(runtime):
    run(testscript="example_script.py", runtime=runtime, groups=non_traffic_sanities)


### Using logic testing at runtime ###

from pyats.easypy import run

# import the logic objects
from pyats.datastructures.logic import And, Not


# same as above, run sanity non-traffic testcases
def main():
    run("example_script.py", groups=And("sanity", Not("traffic")))
