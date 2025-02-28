class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        hashmap_st = {}
        hashmap_ts = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in hashmap_st and hashmap_st[char_s] != char_t: # if S' character is IN the S->T hashmap and not equal to T's character
                return False

            if char_t in hashmap_ts and hashmap_ts[char_t] != char_s: # if T's character is IN the T->S hashmap and not equal to S's character
                return False

            hashmap_st[char_s] = char_t
            hashmap_ts[char_t] = char_s


        return True

# note len(s) strictly == len(t)
# Time: O(n) -> our code does one pass, n iterations
# Space: O(n) -> again s and t are the exact same size so n*2 -> n