# Time O(n) -> at most n iterations
# Space O(1) -> constant space
# Trick is to iterate backwards and get your left and right pointers in the appropriate starting places

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1 and s[0] == "_":
            return 0
        if len(s) == 1 and s[0].isalpha():
            return 1

        
        right = -1
        while s[right] == " ": # Move the right pointer to a valid starting place....one is guaranteeed
            right -= 1
            if right < len(s) * -1:
                return 0


        left = right - 1
        while left > (len(s) * -1) -1: # because we are iterating backwards....and 1 indexed not 0 indexed
            if s[left] != " ":
                left -= 1
            else:
                break

        print("left", left, "right", right)

        return abs(left) - abs(right)


