from typing import List
"""
URL: https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
 
Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""

# Take advantage of the fact that we iterate through lists left -> right
# assign "num_i" first before "num_j", if both are assigned and there 
# is a new num bigger than both return True
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        num_i = num_j = float('inf')
        for num in nums:
            if num <= num_i:
                num_i = num
            elif num <= num_j:
                num_j = num
            else:
                return True
        return False