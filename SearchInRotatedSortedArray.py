"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104


Follow up: Can you achieve this in O(log n) time complexity?
"""
def search(nums, target):
    first = 0
    last = len(nums) - 1

    while first <= last:
        mid = (first + last) // 2

        if target == nums[mid]:
            print('The index of target is: ', end='')
            return mid

        if nums[first] <= nums[mid]:
            if target < nums[first] or target > nums[mid]:
                first = mid + 1
            else:
                last = mid - 1
        else:
            if target < nums[mid] or target > nums[last]:
                last = mid - 1
            else:
                first = mid + 1
    return -1


def seq_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return nums.index(nums[target])
        else:
            continue

    return False


print(search([4,5,6,7,0,1,2], 0))
print(seq_search([1, 3, 2, 6, 4], 2))
