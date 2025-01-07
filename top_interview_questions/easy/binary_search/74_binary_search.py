"""
URL: https://leetcode.com/problems/binary-search/description/
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
 
Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

from typing import List

# Optimal - self
# Time O(logn)
# Space O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left/right/middle are integers
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left)//2
            if nums[middle] < target:
                left = middle + 1 
            elif nums[middle] > target:
                right = middle - 1
            else: # they are equal
                return middle

        return -1
                