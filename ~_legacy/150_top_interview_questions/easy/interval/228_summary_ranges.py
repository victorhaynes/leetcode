class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        solution = []
        right = 0

        while right < len(nums):
            left = right

            while right < len(nums) - 1 and nums[right+1] == nums[right] + 1: # Use while to expand "window" to the right but make sure it is in bounds.
                right += 1

            if left == right:
                solution.append(str(nums[left]))
            else:
                solution.append(f"{nums[left]}->{nums[right]}")

            right += 1

        return solution

# Time O(n)
# Space O(n)