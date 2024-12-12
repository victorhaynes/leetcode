"""
URL: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


# Time O(n)
# Space O(n) bc we need a copy of s with is length n and because words is a factor of n
class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()
        words = []
        word = ""
        for i,char in enumerate(s):
            if char != " ":
                word += char
            if char == " ":
                if word:
                    words.append(word)
                    word = ""
        
        if word: # if anything is left over (which happens because you won't hit a space if a word is the last portion of the string)
            words.append(word)

        solution = ""
        i = len(words) - 1
        while i >= 0:
            solution += words[i] + " "
            i -= 1

        return solution.strip()