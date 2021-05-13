"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
"""


def swap(nums, idx1, idx2):
    temp = nums[idx1]
    nums[idx1] = nums[idx2]
    nums[idx2] = temp


def nextPermutation(nums):
    length = len(nums)
    pointer = length - 2

    if length <= 2:
        nums.reverse()
        return nums

    while nums[pointer] >= nums[pointer + 1]:
        pointer -= 1

    if pointer == -1:
        nums.reverse()
        return nums

    for i in range(length - 1, pointer, -1):
        if nums[pointer] < nums[i]:
            swap(nums, pointer, i)
            break

    nums[pointer + 1:] = reversed(nums[pointer+1:])
    return nums


print(nextPermutation([1,7,9,9,8,3]))
print(nextPermutation([1,2,3]))
print(nextPermutation([]))
print(nextPermutation([2]))
print(nextPermutation([3,2,1]))
