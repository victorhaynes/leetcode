class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t):
            return False

        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        
        if i == len(s):
            return True

        return False

# Time O (n+m): in the worst case we must iterate through almost the entirity of both strings to find the solution
# Space O(1)