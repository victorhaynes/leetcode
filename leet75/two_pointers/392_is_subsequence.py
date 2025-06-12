class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        left = 0
        right = 0

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
                right += 1
            else:
                right += 1


        return left == len(s) # s pointer got to the end of left


    # Time O(max(n,m))
    # space O(1)