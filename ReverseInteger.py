def reverse1( x):
    if not x:
        return x
    sign = x/abs(x)
    x *= sign
    res = 0
    while x:
        res = res*10 + x%10
        x /= 10
    if res < 1<<31:
        return res*sign
    else:
        return 0


print (reverse1(-120))

def reverse(x):
    y = str(abs(x))
    y = y.strip()
    y = y[::-1]

    output = int(y)

    if output > 2**31 -1 or output < -2**31:
        return 0
    elif x< 0:
        return -1* output
    else:
        return output


print (reverse(-1201))