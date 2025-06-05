"""
URL: https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
Follow up: Could you minimize the total number of operations done?

"""


# Optimal O(n) time, O(1) space
# takeaways: python can assign multiple values at the same time (for the swap), but if you do not use the syntax 
# information will be destroyed so you would need temporary varaibles
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) < 2:
            return None

        l = 0
        for r in range(len(nums)):
            if nums[r]:
                # using python's inline tuple assignemnt
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

                # without inline assingment, need temporary variables because values get destroyed
                # templ = nums[l]
                # tempr = nums[r]
                # nums[r] = templ
                # nums[l] = tempr
                # l += 1
