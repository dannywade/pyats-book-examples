from pyats.async_ import pcall


# multiply function that is run in parallel
def multiply(num1, num2):
    return num1 * num2


result = pcall(multiply, num1=(1, 2, 3), num2=(7, 8, 9))

print(result)
# (7, 16, 27)
