def fib(n, memoize = {1:0, 2: 1}):

    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib(n-1, memoize) + fib(n-2, memoize)
        return memoize[n]


print(fib(6, memoize={1:0, 2: 1}))
