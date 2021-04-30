# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.

def maxArea(height):
    largest = 0
    start = 0
    end = len(height) - 1

    while start != end:

        current_area = min(height[start], height[end]) * (end - start)

        if largest < current_area:
            largest = current_area

        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return largest


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 2, 1]))
print(maxArea([4, 3, 2, 1, 4]))
