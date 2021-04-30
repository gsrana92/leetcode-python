"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def lengthOfLongestSubstring(s):
    maximum = 0
    stack = []

    for i in list(s):
        if i not in stack:
            stack.append(i)

        else:
            if len(stack) > maximum:
                maximum = len(stack)
            stack = stack[stack.index(i) + 1:]
            stack.append(i)

    if maximum < len(stack):
        return len(stack)
    else:
        return maximum


def lengthOfLongestSubstring2(s):
    unique = set()
    count = 0
    out = []

    for letter in range(len(s) - 1):
        if s[letter] != s[letter + 1] and s[letter] not in unique:
            unique.add(s[letter])
            count += 1
        else:
            count = 0

        out.append(count)

    return max(out)


print(lengthOfLongestSubstring2('abcabcabc'))
print(lengthOfLongestSubstring('pwwkew'))
