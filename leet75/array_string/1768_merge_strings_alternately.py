class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        solution = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            solution.append(word1[i])
            solution.append(word2[j])
            i += 1
            j += 1

        if i < len(word1):
            while i < len(word1):
                solution.append(word1[i])
                i += 1
        elif j < len(word2):
            while j < len(word2):
                solution.append(word2[j])
                j += 1

        return "".join(solution)
    
    # O(n+m) Time, loop is gated by O(max(n,m)) but every character is touched and n & m can approach different sized infinities
    # O(n+m) Space