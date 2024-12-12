"""
URL: https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

# Optimal - intuition / memory
# time O(n) or O(max(str1, str2))
# space O(1) variables do not grow with the input (necessarily)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            shorter = str1
            longer = str2
        else:
            shorter = str2
            longer = str1

        original_shorter = shorter
        while len(shorter) > 0:
            if len(longer) % len(shorter) == 0 and len(original_shorter) % len(shorter) == 0:
                # if the remainder is 0 for both longer / shorter (i.e. ABCDEF (6) and XY (2) 6/2=3.0)
                # and original_shorter / shorter
                if shorter * int(len(longer) / len(shorter)) == longer and shorter * int(len(original_shorter) / len(shorter)) == original_shorter:
                    return shorter
            shorter = shorter[:-1] # remove the last element if the division isn't clean

        return ""