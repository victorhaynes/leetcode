class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        curr_count = 0
        for char in s[:k]:
            if char in vowels: 
                curr_count += 1

        max_count = curr_count
        left = 0
        for right in range(k, len(s)):
            if s[left] in vowels: 
                curr_count -= 1
            if s[right] in vowels: 
                curr_count += 1
            max_count = max(max_count, curr_count)
            left += 1

        return max_count

# Time O(n), fixed sliding window. one pass
# Space O(1), constant space

""" Fixed sliding window basic outline:
- pre compute something for initial window
- left = 0, for right in range(k, len(nums)):
- some conditional(s)
- left += 1

"""