from pyats.easypy import run

# To run job:
# pyats run job ex0918_pyats_job.py --testbed-file testbed2.yaml --trigger-datafile ex0917_trigger_datafile.yaml --verification-datafile ex0917_verification_datafile.yaml

# All run() must be inside a main function
def main():

    # Execute the testscript
    run(testscript="ex0918_pyats_testscript.py")