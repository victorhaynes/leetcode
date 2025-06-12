class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        zero_count = 0
        max_len = 0

        left = 0
        for right in range(len(nums)):
            if nums[right] == 0: # conditional
                zero_count += 1
            
            while zero_count > 1: # validity enforcement/shrinking or expanding action
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1 - zero_count) # update

        if zero_count:
            return max_len
        else:
            return max_len - 1

# Time O(n), vists each element at most twice time
# space O(1) constant

""" 4 parts to a variable sliding window solution
1) left, for right in range(len(nums))
2) some conditional
3) while loop to enforce validity
4) some update
"""