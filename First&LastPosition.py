"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


def searchRange( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    left = binarySearch(nums, target, True)
    right = binarySearch(nums, target, False)
    return [left, right]


def binarySearch( nums, target, leftBias):
    l = 0
    r = len(nums) - 1
    i = -1

    while l <= r:
        mid = (l + r) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            i = mid
            if leftBias:
                r = mid - 1
            else:
                l = mid + 1
    return i

print(searchRange([5, 7, 7, 8, 8, 10], 8))
print(searchRange([5, 7, 7, 8, 8, 10], 18))
print(searchRange([8], 8))


