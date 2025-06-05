class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern):
            return False

        hashmap_ps = {}
        hashmap_sp = {}

        i = 0
        j = 0
        while i < len(pattern) and j < len(s):
            if pattern[i] in hashmap_ps and hashmap_ps[pattern[i]] !=  s[j]:
                return False
            
            if s[j] in hashmap_sp and hashmap_sp[s[j]] != pattern[i]:
                return False

            hashmap_ps[pattern[i]] = s[j]
            hashmap_sp[s[j]] = pattern[i]

            
            i += 1
            j += 1


        return True

# Time O(n) -> where in the worst case n is the longer of the 2 inputs for the .split() operation
# Space O(n+m) -> 
# two hashmaps 
# first: up to 26 keys: each value can have size m where m is the average length of the word -> O(1) * O(m) == O(m)
# second: up to 26 keys: each key can have size m where m is the avg length of the word, each value is a single character -> O(m)
# split operation takes up O(n) space