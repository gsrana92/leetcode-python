# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);


def zigZagConversion(s, numRows):
    res = [''] * numRows

    row = 0

    if numRows == 1 or numRows > len(s):
        return s

    for char in s:
        res[row] += char

        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1
        row += step
    return ''.join(res)


print(zigZagConversion('PAYPALISHIRING', 3))
print(zigZagConversion('PAYPALISHIRING', 4))

