"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"


Constraints:

1 <= n <= 30
"""


def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i+1< len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count)+ s[i])
        i += 1
    return "".join(result)


def countAndSay(n):
    if n == 1:
        return '1'
    else:
        s = '1'
        for i in range(n-1):
            s = next_number(s)
    return s


print(countAndSay(4))

def countAnsSay2(n):
    if n == 1:
        return '1'
    prev = countAnsSay2(n-1)
    count = 1
    result = ''
    print("prev is: ", prev)

    for i in range(len(prev)):
        if i == len(prev)-1 or prev[i] != prev[i+1]:
            result += str(count) + prev[i]
            print('result is: ', result)
            count = 1
        else:
            count += 1

    return result

print(countAnsSay2(4))








