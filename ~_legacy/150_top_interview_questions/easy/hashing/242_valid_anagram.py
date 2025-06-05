class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap_s = {}
        for char in s:
            if char in hashmap_s:
                hashmap_s[char] += 1
            else:
                hashmap_s[char] = 1
            

        hashmap_t = {}
        for char in t:
            if char in hashmap_t:
                hashmap_t[char] += 1
            else:
                hashmap_t[char] = 1

        for key in hashmap_s:
            if key not in hashmap_t or hashmap_s[key] != hashmap_t[key]:
                return False

        return True

    # Time O(n) -> N times two number of iteration -> 2N == N
    # Space O(1) -> we create 2 hashmaps and put n characters in them but n can only be as large as 26 due to the constraints