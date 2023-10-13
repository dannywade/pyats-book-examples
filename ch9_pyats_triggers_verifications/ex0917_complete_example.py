from genie.harness.main import gRun

# To run job:
# pyats run job ex0917_complete_example.py  --testbed-file testbed2.yaml


def main():
    gRun(
        trigger_uids=["TriggerShutNoShutOspf"],
        trigger_datafile="ex0917_trigger_datafile.yaml",
        verification_uids=["Verify_IpOspfDatabaseRouter"],
        verification_datafile="ex0917_verification_datafile.yaml",
    )


### SAMPLE OUTPUT ###
# 2023-08-08T23:01:49: %EASYPY-INFO: Overall Stats
# 2023-08-08T23:01:49: %EASYPY-INFO:     Passed     : 7
# 2023-08-08T23:01:49: %EASYPY-INFO:     Passx      : 0
# 2023-08-08T23:01:49: %EASYPY-INFO:     Failed     : 0
# 2023-08-08T23:01:49: %EASYPY-INFO:     Aborted    : 0
# 2023-08-08T23:01:49: %EASYPY-INFO:     Blocked    : 0
# 2023-08-08T23:01:49: %EASYPY-INFO:     Skipped    : 0
# 2023-08-08T23:01:49: %EASYPY-INFO:     Errored    : 0
# 2023-08-08T23:01:49: %EASYPY-INFO:
# 2023-08-08T23:01:49: %EASYPY-INFO:     TOTAL      : 7
# 2023-08-08T23:01:49: %EASYPY-INFO:
# 2023-08-08T23:01:49: %EASYPY-INFO: Success Rate   : 100.00 %
# 2023-08-08T23:01:49: %EASYPY-INFO:
# 2023-08-08T23:01:49: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-08T23:01:49: %EASYPY-INFO: |                             Task Result Summary                              |
# 2023-08-08T23:01:49: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-08T23:01:49: %EASYPY-INFO: Task-1: genie_testscript.common_setup                                     PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: Task-1: genie_testscript.Verifications.TriggerShutNoShutOspf.iosv-0       PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: Task-1: genie_testscript.TriggerShutNoShutOspf.iosv-0                     PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: Task-1: genie_testscript.Verifications.TriggerShutNoShutOspf.iosv-1       PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: Task-1: genie_testscript.TriggerShutNoShutOspf.iosv-1                     PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: Task-1: genie_testscript.Verifications.post                               PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: Task-1: genie_testscript.common_cleanup                                   PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO:
# 2023-08-08T23:01:49: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-08T23:01:49: %EASYPY-INFO: |                             Task Result Details                              |
# 2023-08-08T23:01:49: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-08T23:01:49: %EASYPY-INFO: Task-1: genie_testscript
# 2023-08-08T23:01:49: %EASYPY-INFO: |-- common_setup                                                          PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- connect                                                           PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- configure                                                        SKIPPED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- configuration_snapshot                                            PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- save_bootvar                                                      PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- learn_system_defaults                                             PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- initialize_traffic                                               SKIPPED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   `-- PostProcessor-1                                                   PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |-- Verifications.TriggerShutNoShutOspf.iosv-0                            PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- Verify_IpOspfDatabaseRouter.iosv-0.1                              PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |   `-- verify                                                        PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   `-- Verify_IpOspfDatabaseRouter.iosv-1.1                              PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |       `-- verify                                                        PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |-- TriggerShutNoShutOspf.iosv-0                                          PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- prerequisites                                                     PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- ShutOspf                                                          PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- verify_ShutOspf                                                   PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- NoShutOspf                                                        PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   `-- verify_NoShutOspf                                                 PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |-- Verifications.TriggerShutNoShutOspf.iosv-1                            PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- Verify_IpOspfDatabaseRouter.iosv-0.2                              PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |   `-- verify                                                        PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   `-- Verify_IpOspfDatabaseRouter.iosv-1.2                              PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |       `-- verify                                                        PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |-- TriggerShutNoShutOspf.iosv-1                                          PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- prerequisites                                                     PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- ShutOspf                                                          PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- verify_ShutOspf                                                   PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- NoShutOspf                                                        PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   `-- verify_NoShutOspf                                                 PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |-- Verifications.post                                                    PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |-- Verify_IpOspfDatabaseRouter.iosv-0.3                              PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   |   `-- verify                                                        PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |   `-- Verify_IpOspfDatabaseRouter.iosv-1.3                              PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: |       `-- verify                                                        PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO:     |-- verify_configuration_snapshot                                     PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO:     |-- stop_traffic                                                     SKIPPED
# 2023-08-08T23:01:49: %EASYPY-INFO:     `-- PostProcessor-1                                                   PASSED
# 2023-08-08T23:01:49: %EASYPY-INFO: Sending report email...
# 2023-08-08T23:01:49: %EASYPY-INFO: Missing SMTP server configuration, or failed to reach/authenticate/send mail. Result notification email failed to send.
# 2023-08-08T23:01:50: %EASYPY-INFO: Done!
