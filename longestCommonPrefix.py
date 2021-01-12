"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longestCommonPrefix(strs):
    if len(strs) == 0:
        print ''
        return ''

    minlen = len(strs[0])

    for i in range(len(strs)):
        minlen = min(minlen, len(strs[i]))

    lcp = ''

    i = 0
    while i < minlen:
        char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                print lcp
                return lcp
        lcp = lcp + char
        i = i + 1

    print lcp

    return lcp


longestCommonPrefix(['dogma', 'doguer', 'dogs'])
longestCommonPrefix(["flower", "flow", "flight"])
longestCommonPrefix(["dog","racecar","car"])
