from pyats.async_ import Pcall


# define a function to be called in
def add(x, y):
    return x + y


# create a Pcall object
p = Pcall(add, x=(1, 2, 3), y=(4, 5, 6))

# start all child processes
p.start()

# wait for everything to finish
p.join()

# collect results
results = p.results

print(results)
# (5, 7, 9)
