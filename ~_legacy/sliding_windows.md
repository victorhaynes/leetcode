# 2 types

## Fixed window
- Often involes precomputing something
- slide window with `for i in range(k, len(input))`
```py
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        sum_window = sum(nums[:k])
        max_avg = sum_window/k

        print(sum_window)
        for i in range(k, len(nums)):
            sum_window = sum_window - nums[i - k] + nums[i]
            max_avg = max(max_avg, sum_window/k)
            print(sum_window, sum_window/k)


        return max_avg
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