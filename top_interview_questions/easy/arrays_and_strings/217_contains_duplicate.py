from typing import List
"""
URL: https://leetcode.com/problems/contains-duplicate/submissions/1475616332/
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


# Just take advantage of the fact that a set has no duplicates
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cleaned_nums = set(nums)
        if len(nums) != len(cleaned_nums):
            return True
        return False
# time: O(n) takes n time to create a set of length n (len() checks are constant O(1))
# space: O(n) size n set needs creations and storage in memory