# Import Genie run
from genie.harness.main import gRun

# To run job:
# pyats run job ex0916_custom_trigger_job.py  --testbed-file testbed2.yaml

def main():
    gRun(
        trigger_uids=["TriggerMyShutNoShutOspf"],
        trigger_datafile="ex0915_custom_trigger_datafile.yaml",
    )






### SAMPLE OUTPUT ###
# 2023-08-03T23:26:09: %EASYPY-INFO: Overall Stats
# 2023-08-03T23:26:09: %EASYPY-INFO:     Passed     : 4
# 2023-08-03T23:26:09: %EASYPY-INFO:     Passx      : 0
# 2023-08-03T23:26:09: %EASYPY-INFO:     Failed     : 0
# 2023-08-03T23:26:09: %EASYPY-INFO:     Aborted    : 0
# 2023-08-03T23:26:09: %EASYPY-INFO:     Blocked    : 0
# 2023-08-03T23:26:09: %EASYPY-INFO:     Skipped    : 0
# 2023-08-03T23:26:09: %EASYPY-INFO:     Errored    : 0
# 2023-08-03T23:26:09: %EASYPY-INFO: 
# 2023-08-03T23:26:09: %EASYPY-INFO:     TOTAL      : 4
# 2023-08-03T23:26:09: %EASYPY-INFO: 
# 2023-08-03T23:26:09: %EASYPY-INFO: Success Rate   : 100.00 %
# 2023-08-03T23:26:09: %EASYPY-INFO: 
# 2023-08-03T23:26:09: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T23:26:09: %EASYPY-INFO: |                             Task Result Summary                              |
# 2023-08-03T23:26:09: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T23:26:09: %EASYPY-INFO: Task-1: genie_testscript.common_setup                                     PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: Task-1: genie_testscript.TriggerMyShutNoShutOspf.iosv-0                   PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: Task-1: genie_testscript.TriggerMyShutNoShutOspf.iosv-1                   PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: Task-1: genie_testscript.common_cleanup                                   PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: 
# 2023-08-03T23:26:09: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T23:26:09: %EASYPY-INFO: |                             Task Result Details                              |
# 2023-08-03T23:26:09: %EASYPY-INFO: +------------------------------------------------------------------------------+
# 2023-08-03T23:26:09: %EASYPY-INFO: Task-1: genie_testscript
# 2023-08-03T23:26:09: %EASYPY-INFO: |-- common_setup                                                          PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- connect                                                           PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- configure                                                        SKIPPED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- configuration_snapshot                                            PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- save_bootvar                                                      PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- learn_system_defaults                                             PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- initialize_traffic                                               SKIPPED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   `-- PostProcessor-1                                                   PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |-- TriggerMyShutNoShutOspf.iosv-0                                        PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- prerequisites                                                     PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- ShutOspf                                                          PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- verify_ShutOspf                                                   PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- NoShutOspf                                                        PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   `-- verify_NoShutOspf                                                 PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |-- TriggerMyShutNoShutOspf.iosv-1                                        PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- prerequisites                                                     PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- ShutOspf                                                          PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- verify_ShutOspf                                                   PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   |-- NoShutOspf                                                        PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: |   `-- verify_NoShutOspf                                                 PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO:     |-- verify_configuration_snapshot                                     PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO:     |-- stop_traffic                                                     SKIPPED
# 2023-08-03T23:26:09: %EASYPY-INFO:     `-- PostProcessor-1                                                   PASSED
# 2023-08-03T23:26:09: %EASYPY-INFO: Sending report email...
# 2023-08-03T23:26:09: %EASYPY-INFO: Missing SMTP server configuration, or failed to reach/authenticate/send mail. Result notification email failed to send.
# 2023-08-03T23:26:10: %EASYPY-INFO: Done!