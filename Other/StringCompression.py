"""
Given a string in the form 'AAABBBCCCDDDDEEEE' compress it to become 'A3B3C3D4E4'. For this problem you can
falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1'
even though it takes more space. The function should also be case sensitive i.e 'AAAaaa' returns 'A3a3'
"""

def string_compress(s):
    count = 1
    result = ''
    i = 0

    while s[i] == s[i+1]:
        result += s[i]
        count += 1
    for i in range(len(s)-1):
        while s[i] == s[i+1]:
            count += 1
            result += s[i]
            result += str(count)
        count = 1
    return result

print(string_compress('AAABBBCCCaa'))

