# 2 types

## Fixed window
- Often involes precomputing something
- slide window with `for i in range(k, len(input))`
- need to think hard about the edges of the window. For 643. we need the first index of the last window, and the index (right bound) of the new window
```py
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        left = 0
        for right in range(k, len(nums)):                       """This is the basic setp for a window of size = k """
            window_sum = window_sum - nums[left] + nums[right]
            max_sum = max(max_sum, window_sum)
            left += 1
        
        return max_sum / k


# Time O(n) -> sum is O(k<n) time, then n-k iterations -> n time
# Space O(1)      
```

## Varaible window
- L and R start at index 0
- move window with `for right in range(len(input))`
- 1) keep track of something
- 2) use `while` until window becomes valid (shrink window with left pointer)
- 3) perform any calculation for the given `right` pointer after validity is checked/enforced
```py
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # Variable sliding window, start L and R at index 0
        max_len = 0
        zero_count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0: # keep track of the condition in the problem statement
                zero_count += 1

            while zero_count > k: # do work until window becomes valid
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            current_len = right - left + 1 # update the max
            max_len = max(current_len, max_len)

    
        return max_len
```