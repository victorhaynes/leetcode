from typing import List
"""
URL: https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""
# Optimal
# Time O(n) = O(n) for loop and amoritized O(n) for while loop inside of outer loop
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # Variable sliding window, start L and R at index 0
        max_len = 0
        zero_count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0: # keep track of the condition in the problem statement
                zero_count += 1

            while zero_count > k: # do work until window becomes valid
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            current_len = right - left + 1 # update the max
            max_len = max(current_len, max_len)

    
        return max_len