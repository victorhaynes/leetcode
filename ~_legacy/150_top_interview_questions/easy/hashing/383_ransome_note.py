class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hashmap_r = {}
        hashmap_m = {}


        for char in ransomNote:
            if hashmap_r.get(char):
                hashmap_r[char] += 1
            else:
                hashmap_r[char] = 1

        for char in magazine:
            if hashmap_m.get(char):
                hashmap_m[char] += 1
            else:
                hashmap_m[char] = 1


        
        for char in hashmap_r:
            if not hashmap_m.get(char) or not hashmap_m.get(char) >= hashmap_r[char]:
                return False

        return True

# Time: O(n+m) takes n time and m time to build the hashmaps, then we do n iterations of constant work
# Space: O(1) -> BECAUSE we have the constraint that ransomeNote and magazine are made up of lowercase english letters...so worst case the hashmaps are O(26 + 26) == O(1) constant size. Not n or m
# without this constraint it would be O(n+m) where n and m are the size of the strings/hashmaps