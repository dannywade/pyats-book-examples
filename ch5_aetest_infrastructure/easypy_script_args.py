from pyats.easpy import run


def main():
    run(
        testscript="standalone_exec_input_args.py",
        pyats_is_awesome=True,
        aetest_is_legendary=True,
    )


# Run the easypy job
# pyats run job easypy_script_args.py --testbed ../testbed.yaml
