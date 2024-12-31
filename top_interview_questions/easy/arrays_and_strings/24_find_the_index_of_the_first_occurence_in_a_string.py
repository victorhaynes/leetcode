"""
URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

# Optimal
# Time O(n * m) where n is the longer word and m is the shortest in the worst case
# Space O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        potential_solution = 0 # starting index / 1st possible
        i = 0
        j = 0
    

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                potential_solution += 1
                i = potential_solution
                j = 0

            if j == len(needle):
                return potential_solution


        return -1