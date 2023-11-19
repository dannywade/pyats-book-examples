*** Settings ***
# Importing test libraries, resource files and variable files.
Library        pyats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot

*** Variables ***
${testbed}    testbed.yaml

*** Test Cases ***

Initialize
        # Initializes the pyATS/Genie Testbed
        use genie testbed "${testbed}"

        # Connect to 'cat8k-rt1' device
        connect to device "cat8k-rt1"

Learn OSPF
    # Learn OSPF feature from 'cat8k-rt1' device and assign to 'output' variable
    ${output}=    learn "ospf" on device "cat8k-rt1"


# Run it: robot learn_ospf.robot

# Example Output:
# ==============================================================================
# Learn Ospf                                                                    
# ==============================================================================
# Initialize                                                            | PASS |
# ------------------------------------------------------------------------------
# Learn OSPF                                                            | PASS |
# ------------------------------------------------------------------------------
# Learn Ospf                                                            | PASS |
# 2 tests, 2 passed, 0 failed
# ==============================================================================
# Output:  /Users/danwade/temp/pyats-book-examples/ch11_network_snapshots/robot_framework/output.xml
# Log:     /Users/danwade/temp/pyats-book-examples/ch11_network_snapshots/robot_framework/log.html
# Report:  /Users/danwade/temp/pyats-book-examples/ch11_network_snapshots/robot_framework/report.html