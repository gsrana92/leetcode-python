"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    result = []
    helper(sorted(candidates), result, 0, [], target)
    return result


def helper(candidates, result, start, intermediate, target):
    if target == 0:
        result.append(list(intermediate))
        print(result)
    prev = 0
    while start < len(candidates) and candidates[start] <= target:
        if prev != candidates[start]:
            intermediate.append(candidates[start])
            helper(candidates, result, start+1, intermediate, target - candidates[start])
            intermediate.pop()
            prev = candidates[start]
        start += 1


print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
