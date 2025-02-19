from typing import List
"""
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
"""


# Time O(n) -> loop through once
# Space O(1) -> constant space

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        # Two pointers, LEFT and RIGHT
        # Left keeps track of the modifcation index, right is what goes through the entire array and progresses the iteration

        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1


        return left

        
            

            
