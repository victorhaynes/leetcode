"""
URL: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# Optimal 
# Time O(n x m) ... *unpacking the list takes O(n) the we iterate m times - also note that zip lazily creates the tuples
# Space O(1) - the set is only created
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        solution = ""
        for t in zip(*strs):
            if len(set(t)) == 1:
                solution += t[0]
            else:
                break
            

        return solution