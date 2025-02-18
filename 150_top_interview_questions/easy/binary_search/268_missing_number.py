"""
URL: https://leetcode.com/problems/missing-number/description/

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""
from typing import List

# Optimal - doesn't actully use binary search. If nums was sorted we could beat O(n logn) but we can't because we must sort then do binary search...the sorting dominates
# the sum of the range [0,n] minus the sum of nums [a,b,..z] is the number that is missing from nums
# Time O(N) to sum
# space O(1) memory (remember in python range is stored in memory 1 value at a time so it's never scaled with all of n at once)
class Solution:
    def missingNumber(self, nums:List[int]) -> int:
        sum1 = sum(nums)
        sum2 = sum(range(len(nums) +1))

        solution = sum2 - sum1

        return solution


# Intuition = O(n) time (turn nums into a set, set membership checks are O(1)) 
# Intuition = O(n) space
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         numbers = set(range(len(nums)+1))
#         nums = set(nums)

#         for n in numbers:
#             if n not in nums:
#                 return n


#         return None

        
# # Binary search
# # Time (O(n)logn)
# # Space O(1) (sorting is in place)
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         # Step 1: Sort the array (O(n log n))
#         nums.sort()

#         # Step 2: Apply binary search (O(log n))
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             # If the value at mid matches the index, search to the right
#             if nums[mid] == mid:
#                 left = mid + 1
#             else:
#                 # Otherwise, search to the left
#                 right = mid - 1

#         # The missing number is at index `left`
#         return left
