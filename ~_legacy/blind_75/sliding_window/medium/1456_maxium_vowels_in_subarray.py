"""
URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s) == 1:
            if k == 1:
                return 1
            else:
                raise Exception
        
        
        vowels = ['a', 'e', 'i', 'o', 'u']

        maximum = float('-inf')
        initial_count = 0
        sub_array = s[:k]
        for char in sub_array:
            if char.lower() in vowels:
                initial_count += 1

        if initial_count == len(s):
            return k

        count = initial_count
        for i in range(k, len(s)):
            if s[i-k].lower() in vowels:
                count -= 1
            if s[i].lower() in vowels:
                count += 1
            print(count)
            maximum = max(maximum, count, initial_count)

        return maximum