from typing import List
"""
URL: https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.


Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 
"""


# Optimal
# Time O(n*log(n)) bc of the sorting
# Space O(log(n)) bc of the sorting
# Don't be afraid to sort lists to take advantage of their increasing number properties when it comes to math problems
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() # sort the list from low to high O(n * log (n)) time, uses O(log(n)) memory
        operations = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum == k:
                operations += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1 # Increase sum by sliding pointer to the right, take advantage of sorting
            elif current_sum > k:
                right -= 1 # Decrease sum by sliding pointer to the left, take advantage of sorting
            else:
                raise Exception("Uncaught Scenario")

        return operations
