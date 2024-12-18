from typing import List
"""
URL: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

"""
# Optimal
# Time O(n) = O(n) for loop and amoritized O(n) for while loop inside of outer loop
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0 # problem asks for a max, we need to initialize a max
        zero_count = 0 
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1: # force/check validity
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            current_len = (right - left + 1) - 1 # perform max update for this iteration, note we use - 1 bc the prompt says to delete an element
            max_len = max(max_len, current_len)

        if max_len:
            return max_len
        else:
            return 0
