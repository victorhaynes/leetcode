class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # or do a cheeky sorted().... runs in O(nlogn + mlogm) time and O(1) space
        # return sorted(s) == sorted(t)


        if len(s) != len(t):
            return False

        hashmap1 = {}
        hashmap2 = {}

        i,j = 0,0
        while i < len(s) and j < len(t):
            try:
                hashmap1[s[i]] += 1
            except KeyError:
                hashmap1[s[i]] = 1
            i += 1

            try:
                hashmap2[t[j]] += 1
            except KeyError:
                hashmap2[t[j]] = 1
            j += 1

        
        for char in s:
            try:
                if hashmap1[char] != hashmap2[char]: # compare counts in the hashmap
                    return False
            except KeyError:
                return False

        return True

# Time: O(n+m) -> where n and m are the length of the two strings
# ....Space: O(n+m) -> need two hashmaps each of size n and size m
# BUT DUE TO THE CONSTRAINT:
# Space: O(1) -> hashmaps can only be up to size 26 units (lowercase english alphabet, no repeats in the hasmap)
