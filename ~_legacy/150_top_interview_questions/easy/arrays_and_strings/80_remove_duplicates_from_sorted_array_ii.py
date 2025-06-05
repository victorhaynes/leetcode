class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 1
        right = 1

        count = 1
        while right < len(nums): # only move left when something valid happens nums[right]
            if count < 2 and nums[right] == nums[right - 1]: # if the current value is the same as the prev value but it is below the limit
                count += 1
                nums[left] = nums[right]
                left += 1
            elif nums[right] != nums[right - 1]: # if it is a new number it is valid, start count at 1
                count = 1
                nums[left] = nums[right]
                left += 1
            else:
                print("safety check, but this should never happen")
            
            right += 1

        return left

# Time O(n) -> n iterations through nums
# Space O(1) -> constant space/inplace algorithm
# Idea here: put your pointers at places that make sense given the problem along with any other variables, and start them at same location