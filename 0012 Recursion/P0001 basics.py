# --------------------------------
# Using iterative factorial
# --------------------------------
def iterativeFactorial(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i
    return result


print(iterativeFactorial(5))  # 120


# --------------------------------
# How to Do it recursively
# Calling function again and again
# --------------------------------


def recursiveFactorial(n):
    if n == 0:  # we need this to stop a recursion if n hits 0
        return 1
    else:
        return n * recursiveFactorial(n-1)


print(recursiveFactorial(5))  # 120
