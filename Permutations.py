"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""


def stringPermute(s):
    out = []
    if len(s) == 1:
        out = [s]

    else:
        for i, let in enumerate(s):

            for perm in stringPermute(s[:1] + s[i + 1:]):
                out += [let + perm]

    return out


# print(stringPermute('abc'))


def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        print(perms)

        for perm in perms:
            # print(perm)
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result


# print(permute([1, 2, 3]))


def permute2(nums):
    result = []

    if len(nums) == 1:
        return [nums]

    for i in range(len(nums)):
        x = nums[i]
        print('x is: ', x)
        xs = nums[:i] + nums[i + 1:]
        print('xs is :', xs)

        for perm in permute2(xs):
            print('perm is : ', perm)
            result.append([x] + perm)
            print('result is: ', result)
            print('***********step complete***********')
    return result


print(permute2([1, 2, 3]))


def permute3(s):

    result = []

    if len(s) == 1:
        return [s]

    for i in range(len(s)):
        x = s[i]
        xs = s[:i] + s[i+1:]

        for perm in permute3(xs):
            result.append(x+perm)
    return result


print(permute3('abc'))