def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    copyOfDividend = abs(dividend)
    copyOfDivisor = abs(divisor)
    output = 0

    while copyOfDividend >= copyOfDivisor:
        temp = copyOfDivisor
        mul = 1

        while copyOfDividend >= temp:
            copyOfDividend -= temp
            output += mul
            mul += mul
            temp += temp

    if dividend < 0 and divisor >= 0 or dividend >= 0 and divisor < 0:
        output = -output

    return min(2 ** 31 - 1, max(output, -2 ** 31))


print(divide(2 ** 31, -1))
print(divide(10, 3))
print(divide(2**31, 1))
