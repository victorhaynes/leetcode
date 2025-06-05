"""
URL: https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
"""

# Optimal Time O(n)
# Space O(n) because strings are not mutable in python, if they were you could operate in place and not use a hashmap
class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 0:
            return s

        solution = ""
        hashmap = {}
        i = 0
        j = len(s) - 1

        while i < j:
            left_letter = s[i].lower()
            right_letter = s[j].lower()

            if left_letter in ["a","e","i",'o',"u"] and right_letter in ["a","e","i",'o',"u"]:
                hashmap[i] = s[j]
                hashmap[j] = s[i]
                i += 1
                j -= 1
            if left_letter in ["a","e","i",'o',"u"] and right_letter not in ["a","e","i",'o',"u"]:
                j -= 1
            if left_letter not in ["a","e","i",'o',"u"] and right_letter in ["a","e","i",'o',"u"]:
                i += 1
            if left_letter not in ["a","e","i",'o',"u"] and right_letter not in ["a","e","i",'o',"u"]:
                i += 1
                j -= 1


        for i, char in enumerate(s):
            if i in hashmap:
                solution+=hashmap[i]
                continue
            else:
                solution+=char

        return solution