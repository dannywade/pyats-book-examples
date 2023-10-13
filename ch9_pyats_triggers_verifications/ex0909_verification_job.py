# Import Genie run
from genie.harness.main import gRun

# To run job:
# pyats run job ex0909_verification_job.py --testbed-file testbed.yaml


def main():
    gRun(
        verification_uids=["Verify_Interfaces"],
        verification_datafile="ex0908_verification_datafile.yaml",
    )


### SAMPLE OUTPUT ###
# 2023-08-03T22:50:39: %EASYPY-INFO: Overall Stats
# 2023-08-03T22:50:39: %EASYPY-INFO:     Passed     : 3
# 2023-08-03T22:50:39: %EASYPY-INFO:     Passx      : 0
# 2023-08-03T22:50:39: %EASYPY-INFO:     Failed     : 0
# 2023-08-03T22:50:39: %EASYPY-INFO:     Aborted    : 0
# 2023-08-03T22:50:39: %EASYPY-INFO:     Blocked    : 0
# 2023-08-03T22:50:39: %EASYPY-INFO:     Skipped    : 0
# 2023-08-03T22:50:39: %EASYPY-INFO:     Errored    : 0
# 2023-08-03T22:50:39: %EASYPY-INFO:
# 2023-08-03T22:50:39: %EASYPY-INFO:     TOTAL      : 3
# 2023-08-03T22:50:39: %EASYPY-INFO:
# 2023-08-03T22:50:39: %EASYPY-INFO: Success Rate   : 100.00 %
# 2023-08-03T22:50:39: %EASYPY-INFO:
# 2023-08-03T22:50:39: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T22:50:39: %EASYPY-INFO: |                             Task Result Summary                              |
# 2023-08-03T22:50:39: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T22:50:39: %EASYPY-INFO: Task-1: genie_testscript.common_setup                                     PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: Task-1: genie_testscript.Verifications.post                               PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: Task-1: genie_testscript.common_cleanup                                   PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO:
# 2023-08-03T22:50:39: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T22:50:39: %EASYPY-INFO: |                             Task Result Details                              |
# 2023-08-03T22:50:39: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T22:50:39: %EASYPY-INFO: Task-1: genie_testscript
# 2023-08-03T22:50:39: %EASYPY-INFO: |-- common_setup                                                          PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: |   |-- connect                                                           PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: |   |-- configure                                                        SKIPPED
# 2023-08-03T22:50:39: %EASYPY-INFO: |   |-- configuration_snapshot                                            PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: |   |-- save_bootvar                                                      PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: |   |-- learn_system_defaults                                             PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: |   |-- initialize_traffic                                               SKIPPED
# 2023-08-03T22:50:39: %EASYPY-INFO: |   `-- PostProcessor-1                                                   PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: |-- Verifications.post                                                    PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: |   |-- Verify_Interfaces.cat8k-rt1.1                                     PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: |   |   `-- verify                                                        PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: |   `-- Verify_Interfaces.cat8k-rt2.1                                     PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: |       `-- verify                                                        PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO:     |-- verify_configuration_snapshot                                     PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO:     |-- stop_traffic                                                     SKIPPED
# 2023-08-03T22:50:39: %EASYPY-INFO:     `-- PostProcessor-1                                                   PASSED
# 2023-08-03T22:50:39: %EASYPY-INFO: Sending report email...
# 2023-08-03T22:50:39: %EASYPY-INFO: Missing SMTP server configuration, or failed to reach/authenticate/send mail. Result notification email failed to send.
# 2023-08-03T22:50:40: %EASYPY-INFO: Done!
