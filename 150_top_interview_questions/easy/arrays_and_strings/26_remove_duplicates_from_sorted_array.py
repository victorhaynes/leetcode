class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        # Two pointers, LEFT and RIGHT
        # Left keeps track of the modifcation index, right is what goes through the entire array and progresses the iteration

        # Time O(n) -> loop through once
        # Space O(1) -> constant space

        left = 1
        right = 1

        while right < len(nums):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left

        