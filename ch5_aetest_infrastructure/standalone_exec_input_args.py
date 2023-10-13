from pyats import aetest


class Testcase(aetest.Testcase):
    # defining a test that prints out the current parameters
    # in order to demonstrate argument passing to parameters
    @aetest.test
    def test(self):
        print("Parameters = ", self.parameters)


# do the parsing within the __main__ block,
# and pass the parsed arguments to aetest.main()
if __name__ == "__main__":
    # local imports under __main__ section
    # this is done here because we don't want to pollute the namespace
    # when the script isn't run under standalone
    import sys
    import argparse
    from pyats import topology

    # creating our own parser to parse script arguments
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument("--testbed", dest="testbed", type=topology.loader.load)
    parser.add_argument("--vlan", dest="vlan", type=int)

    # do the parsing
    # always use parse_known_args, as aetest needs to parse any
    # remainder arguments that this parser does not understand
    args, sys.argv[1:] = parser.parse_known_args(sys.argv[1:])

    # and pass all arguments to aetest.main() as kwargs
    aetest.main(testbed=args.testbed, vlan=args.vlan)

# Let's run this script with the following command
# python standalone_exec_input_args.py --testbed ../testbed.yaml -vlan 50


# Example Output:
# 2023-09-21T00:43:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:43:15: %AETEST-INFO: |                          Starting testcase Testcase                          |
# 2023-09-21T00:43:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:43:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:43:15: %AETEST-INFO: |                            Starting section test                             |
# 2023-09-21T00:43:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# Parameters =  ParameterMap({}, {'testbed': <Testbed object 'Cat8k Lab' at 0x7f56e2ed3e80>, 'vlan': None})
# 2023-09-21T00:43:15: %AETEST-INFO: The result of section test is => PASSED
# 2023-09-21T00:43:15: %AETEST-INFO: The result of testcase Testcase is => PASSED
# 2023-09-21T00:43:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:43:15: %AETEST-INFO: |                               Detailed Results                               |
# 2023-09-21T00:43:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:43:15: %AETEST-INFO:  SECTIONS/TESTCASES                                                      RESULT
# 2023-09-21T00:43:15: %AETEST-INFO: --------------------------------------------------------------------------------
# 2023-09-21T00:43:15: %AETEST-INFO: .
# 2023-09-21T00:43:15: %AETEST-INFO: `-- Testcase                                                              PASSED
# 2023-09-21T00:43:15: %AETEST-INFO:     `-- test                                                              PASSED
# 2023-09-21T00:43:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:43:15: %AETEST-INFO: |                                   Summary                                    |
# 2023-09-21T00:43:15: %AETEST-INFO: +------------------------------------------------------------------------------+
# 2023-09-21T00:43:15: %AETEST-INFO:  Number of ABORTED                                                            0
# 2023-09-21T00:43:15: %AETEST-INFO:  Number of BLOCKED                                                            0
# 2023-09-21T00:43:15: %AETEST-INFO:  Number of ERRORED                                                            0
# 2023-09-21T00:43:15: %AETEST-INFO:  Number of FAILED                                                             0
# 2023-09-21T00:43:15: %AETEST-INFO:  Number of PASSED                                                             1
# 2023-09-21T00:43:15: %AETEST-INFO:  Number of PASSX                                                              0
# 2023-09-21T00:43:15: %AETEST-INFO:  Number of SKIPPED                                                            0
# 2023-09-21T00:43:15: %AETEST-INFO:  Total Number                                                                 1
# 2023-09-21T00:43:15: %AETEST-INFO:  Success Rate                                                            100.0%
# 2023-09-21T00:43:15: %AETEST-INFO: --------------------------------------------------------------------------------
