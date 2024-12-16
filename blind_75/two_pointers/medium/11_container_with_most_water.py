from typing import List
"""
URL: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

"""

# Optimal
# Time O(n)
# Space O(1)
# Takeaways: remember the style of 2 points where "while left < right"
# For this problem slide your pointer if it represents a value smaller than the other pointer
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        area = 0
        while left < right:
            print(left, right)
            width = right - left
            calc = width * min(height[left], height[right])
            area = max(area, calc)
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                left += 1
                right -= 1

        return area

        # Brute Force
        # area = 0

        # for l in range(len(height)):
        #     for r in range(l +1, len(height)):
        #         calculation = (r - l) * min(height[l], height[r])
        #         area = max(area, calculation)

        # return area