# This example is just psuedocode and is not meant to be executed

# The following parameters were already defined
parameters = {
    "arg_a": 1,
    "arg_b": 2,
}


# The following inputs were passed as arguments to the testscript
script_arguments = {
    "arg_a": 100,
    "arg_c": 3,
}


# The TestScript parameters would be built as follows
testscript.parameters = parameters
testscript.parameters.update(script_arguments)

# Result - you’ll notice that arg_a was updated by the script arguments
testscript.parameters
# {"arg_a": 100,
#  "arg_b": 2,
#  "arg_c": 3}
