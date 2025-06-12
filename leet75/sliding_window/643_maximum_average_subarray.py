class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        left = 0
        for right in range(k, len(nums)):
            window_sum = window_sum - nums[left] + nums[right]
            max_sum = max(max_sum, window_sum)
            left += 1
        
        return max_sum / k


# Time O(n) -> sum is O(k<n) time, then n-k iterations -> n time
# Space O(1)      