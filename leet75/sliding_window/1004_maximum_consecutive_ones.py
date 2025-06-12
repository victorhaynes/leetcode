class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
    
        zero_count = 0
        max_len = 0

        left = 0 
        for right in range(len(nums)): # left = 0, for right in range(len(nums)) basic sliding window setup
            if nums[right] == 0: # conditional
                zero_count += 1
            
            while zero_count > k: # enforce window validity, shrink/expand
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            current_len = right - left + 1 # 
            max_len = max(max_len, current_len)
        
        return max_len


# Time O(n) -> visit each index at most twice
# Space O(1)