# Anagram Check¶
# Problem
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using
# the exact same letters (so you can just rearrange the letters to get a different phrase or word).
#
# For example:
#
# "public relations" is an anagram of "crap built on lies."
#
# "clint eastwood" is an anagram of "old west action"
# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".


def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if sorted(s1) == sorted(s2):
        return 'Given strings are anagram of each other'
    else:
        return 'Given strings are not anagram of each other'


print(anagram('old west action', 'CLINT EASTWOOD'))


def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return 'Not anagram'

    count = {}

    for letter in s1:
        if letter in count:

            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return 'Not anagram'
    return 'IS Anagram'

print(anagram2('old west action', 'clint eastWOODs'))


