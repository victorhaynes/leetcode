"""
URL: https://leetcode.com/problems/two-sum/description/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List


# Make a hashmap
# Iterate through nums list to once to write all values and their index {3: 0, 6: 1} to hashmap...etc 
# Iterate through nums list against and calculate potential answer (target - num)
# if potential_answer in hashmap and hashmap[potential_answer ] != i 
# then you have solution
# note when you use enumerate(nums) i is the index of num. so return i (not num[i])

# Optimal
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        for i, num in enumerate(nums):
            # target = num + potential_asnwer
            potential_answer = target - num
            if potential_answer in hashmap and hashmap[potential_answer] != i: # the solution can't be the same index's value + itself
                return [i, hashmap[potential_answer]]
        return []
# time O(n)
# space O(n)

# Take aways, keep it simple, write code you understand
# Space complexity does not necessarily include the input
# It only cares about how much is held in memory at any given time (so loop variables do not count but a building list/dict do)
# Use enumerate when not sure because it is versatile

# Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums): # loop through nums with pointer 1
            for j, num2 in enumerate(nums):  # loop through nums with pointer 2
                if i != j and num1 + num2 == target: # ignore case where i == j
                    return [i, j]
# time O(n^2)
# space O(1)


