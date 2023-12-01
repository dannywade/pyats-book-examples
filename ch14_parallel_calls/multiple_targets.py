from pyats.async_ import pcall


# pcall target functions
def func1(*args, **kwargs):
    return dict(name="func1", arg=args, kwargs=kwargs)


def func2(*args, **kwargs):
    return dict(name="func2", arg=args, kwargs=kwargs)


def func3(*args, **kwargs):
    return dict(name="func3", arg=args, kwargs=kwargs)


def print_pcall_results(results: tuple):
    """Loop through pcall results and print each child process' results"""
    for i in range(len(results)):
        print(f"Child process {results.index(results[i]) + 1}: {results[i]}")


# Positional argument building example
parg_results = pcall(
    [func1, func2, func3], cargs=[1, 2, 3], iargs=[[4, 5, 6], [7, 8, 9], [9, 10, 11]]
)
print("Positional args:")
print_pcall_results(parg_results)

# Keyword argument building example
kwarg_results = pcall(
    [func1, func2, func3],
    ckwargs={"a": 1, "b": 2},
    ikwargs=[{"c": 3}, {"c": 4}, {"c": 5}],
)
print(f"\nKeyword args:")
print_pcall_results(kwarg_results)


# Positional args:
# Child process 1: {'name': 'func1', 'arg': (1, 2, 3, 4, 5, 6), 'kwargs': {}}
# Child process 2: {'name': 'func2', 'arg': (1, 2, 3, 7, 8, 9), 'kwargs': {}}
# Child process 3: {'name': 'func3', 'arg': (1, 2, 3, 9, 10, 11), 'kwargs': {}}

# Keyword args:
# Child process 1: {'name': 'func1', 'arg': (), 'kwargs': {'a': 1, 'b': 2, 'c': 3}}
# Child process 2: {'name': 'func2', 'arg': (), 'kwargs': {'a': 1, 'b': 2, 'c': 4}}
# Child process 3: {'name': 'func3', 'arg': (), 'kwargs': {'a': 1, 'b': 2, 'c': 5}}
