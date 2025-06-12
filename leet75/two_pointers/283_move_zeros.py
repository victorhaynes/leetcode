class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) < 2:
            return None

        left = 0
        right = 0 # Trick is for this problem the pointers start at the same position

        while right < len(nums):
            if nums[right] != 0: # Idea is you move all real numbers to the left
                copy = nums[left]
                nums[left] = nums[right]
                nums[right] = copy
                left += 1
            right += 1

    # Time O(n), one pass
    # Space O(1), in place modification