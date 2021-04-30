"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""


def threeSumClosest(nums, target):
    best = 10000
    nums.sort()

    length = len(nums)
    for i in range(length - 2):
        l = i + 1
        r = length - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == target:
                return total
            if abs(target - total) < abs(target - best):
                best = total

            if total < target:
                l += 1
            else:
                r -= 1
    return best


print(threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))
print(threeSumClosest([-1, 2, 1, -4], 1))
