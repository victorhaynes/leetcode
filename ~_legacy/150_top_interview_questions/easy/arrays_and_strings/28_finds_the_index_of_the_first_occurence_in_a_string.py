# Idea: Fixed sliding window?
# Incremental window sliding, look at the window and compare it to the target. if it is correct return left
# Otherwise increment left by one

# Time O(N*M) -> we must do n iterations but in each iteration we do worst m work to slice the haystack to the size of needle
# Space O(1) -> constant space

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        haystack_len = len(haystack)
        needle_len = len(needle)

        if needle_len > haystack_len:
            return -1 # There is no solution

        left = 0 # window start.....the window size is thing[left:left+len(target)]
        while left <= haystack_len - needle_len: # fixed window condition is generally speaking while left <= len(sequennce) - len(subsequence) -> this gives space in front of left for the window size
            if haystack[left:left+needle_len] == needle:
                return left
            left += 1


        return -1