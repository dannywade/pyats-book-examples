from genie.harness.main import gRun

# To run job (Example 9-4): pyats run job ex0904_genie_harness_job.py --testbed-file testbed.yaml

# NOTE: A testbed device must be named or have an alias of 'uut'. Otherwise, a trigger and/or verification datafile must be included in gRun args


def main():
    # Using built-in triggers and verifications
    gRun(trigger_uids=["TriggerSleep"], verification_uids=["Verify_IpInterfaceBrief"])


### SAMPLE OUTPUT ###
# 2023-08-03T22:04:30: %EASYPY-INFO: Overall Stats
# 2023-08-03T22:04:30: %EASYPY-INFO:     Passed     : 5
# 2023-08-03T22:04:30: %EASYPY-INFO:     Passx      : 0
# 2023-08-03T22:04:30: %EASYPY-INFO:     Failed     : 0
# 2023-08-03T22:04:30: %EASYPY-INFO:     Aborted    : 0
# 2023-08-03T22:04:30: %EASYPY-INFO:     Blocked    : 0
# 2023-08-03T22:04:30: %EASYPY-INFO:     Skipped    : 0
# 2023-08-03T22:04:30: %EASYPY-INFO:     Errored    : 0
# 2023-08-03T22:04:30: %EASYPY-INFO:
# 2023-08-03T22:04:30: %EASYPY-INFO:     TOTAL      : 5
# 2023-08-03T22:04:30: %EASYPY-INFO:
# 2023-08-03T22:04:30: %EASYPY-INFO: Success Rate   : 100.00 %
# 2023-08-03T22:04:30: %EASYPY-INFO:
# 2023-08-03T22:04:30: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T22:04:30: %EASYPY-INFO: |                             Task Result Summary                              |
# 2023-08-03T22:04:30: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T22:04:30: %EASYPY-INFO: Task-1: genie_testscript.common_setup                                     PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: Task-1: genie_testscript.Verifications.TriggerSleep.uut                   PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: Task-1: genie_testscript.TriggerSleep.uut                                 PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: Task-1: genie_testscript.Verifications.post                               PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: Task-1: genie_testscript.common_cleanup                                   PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO:
# 2023-08-03T22:04:30: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T22:04:30: %EASYPY-INFO: |                             Task Result Details                              |
# 2023-08-03T22:04:30: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T22:04:30: %EASYPY-INFO: Task-1: genie_testscript
# 2023-08-03T22:04:30: %EASYPY-INFO: |-- common_setup                                                          PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   |-- connect                                                           PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   |-- configure                                                        SKIPPED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   |-- configuration_snapshot                                            PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   |-- save_bootvar                                                      PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   |-- learn_system_defaults                                             PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   |-- initialize_traffic                                               SKIPPED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   `-- PostProcessor-1                                                   PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |-- Verifications.TriggerSleep.uut                                        PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   `-- Verify_IpInterfaceBrief.uut.1                                     PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |       `-- verify                                                        PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |-- TriggerSleep.uut                                                      PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   |-- PreProcessor-1                                                    PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   |-- sleep                                                             PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   |-- PostProcessor-1                                                   PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   |-- PostProcessor-2                                                   PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   `-- PostProcessor-3                                                   PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |-- Verifications.post                                                    PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |   `-- Verify_IpInterfaceBrief.uut.2                                     PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: |       `-- verify                                                        PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO:     |-- verify_configuration_snapshot                                     PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO:     |-- stop_traffic                                                     SKIPPED
# 2023-08-03T22:04:30: %EASYPY-INFO:     `-- PostProcessor-1                                                   PASSED
# 2023-08-03T22:04:30: %EASYPY-INFO: Sending report email...
# 2023-08-03T22:04:30: %EASYPY-INFO: Missing SMTP server configuration, or failed to reach/authenticate/send mail. Result notification email failed to send.
# 2023-08-03T22:04:31: %EASYPY-INFO: Done!
