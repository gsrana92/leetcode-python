def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(5))
# for i in range(1, 101):
#     print(i, fibonacci(i))

"""
MEMOIZATION: Idea is to store the previous call in a cache so we don't have to make more recursive calls
"""
# APPROACH 1 : EXPLICITLY
fib_cache = {}


def fibo(n):
    if n in fib_cache:
        return fib_cache[n]

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        value = fibo(n - 1) + fibo(n - 2)
    fib_cache[n] = value
    return value

print(fibo(100))
for i in range(1, 100):
    print(i, fibo(i))

# APPROACH 2 : PYTHON TOOLS
from functools import lru_cache

@lru_cache(maxsize=1000)
def fib3(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib3(n-1) + fib3(n-2)

print(fib3(100))



