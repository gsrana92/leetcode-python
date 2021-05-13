"""
Write a function that counts the number of ways you can partition n objects using parts upto m(assuming m >=0)
"""


def partition(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0

    else:
        return partition(n - m, m) + partition(n, m - 1)


print(partition(5, 3))
print(partition(4, 3))
