from pyats.async_ import pcall


# pcall target function
def func(*args, **kwargs):
    """Function returns all arguments back"""
    return {"args": args, "kwargs": kwargs}


def print_pcall_results(results: tuple):
    """Loop through pcall results and print each child process' results"""
    for i in range(len(results)):
        print(f"Child process {results.index(results[i]) + 1}: {results[i]}")


# Positional argument building example
parg_results = pcall(func, cargs=(1, 2, 3), iargs=((4,), (5,), (6,)))
print("Positional args:")
print_pcall_results(parg_results)

# Keyword argument building example
kwarg_results = pcall(
    func, ckwargs={"a": 1, "b": 2}, ikwargs=[{"c": 3}, {"c": 4}, {"c": 5}]
)
print(f"\nKeyword args:")
print_pcall_results(kwarg_results)

# Variable keyword argument building example
varkwargs_results = pcall(func, x=(1, 2, 3), y=(4, 5, 6), z=(7, 8, 9))
print(f"\nVariable Keyword args:")
print_pcall_results(varkwargs_results)


# Positional args:
# Child process 1: {'args': (1, 2, 3, 4), 'kwargs': {}}
# Child process 2: {'args': (1, 2, 3, 5), 'kwargs': {}}
# Child process 3: {'args': (1, 2, 3, 6), 'kwargs': {}}

# Keyword args:
# Child process 1: {'args': (), 'kwargs': {'a': 1, 'b': 2, 'c': 3}}
# Child process 2: {'args': (), 'kwargs': {'a': 1, 'b': 2, 'c': 4}}
# Child process 3: {'args': (), 'kwargs': {'a': 1, 'b': 2, 'c': 5}}

# Variable Keyword args:
# Child process 1: {'args': (), 'kwargs': {'x': 1, 'y': 4, 'z': 7}}
# Child process 2: {'args': (), 'kwargs': {'x': 2, 'y': 5, 'z': 8}}
# Child process 3: {'args': (), 'kwargs': {'x': 3, 'y': 6, 'z': 9}}
