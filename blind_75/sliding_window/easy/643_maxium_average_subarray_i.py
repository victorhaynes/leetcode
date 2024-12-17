from typing import List
"""
URL: https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""

# Optimal
# O(n) time
# O(1) space .... not O(k) apparently for the array slicing
# Fixed window sliding window problem (HINT: precompute something then slide)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        sum_window = sum(nums[:k])
        max_avg = sum_window/k

        print(sum_window)
        for i in range(k, len(nums)):
            sum_window = sum_window - nums[i - k] + nums[i]
            max_avg = max(max_avg, sum_window/k)
            print(sum_window, sum_window/k)


        return max_avg