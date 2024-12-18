from typing import List
"""
URL: https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

"""
# Optimal
# Time O(n) - n iterations through arr
# Space O(n) - hashmap of size n, set of size n
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}

        for i, a in enumerate(arr):
            unique_number = hashmap.get(a)
            if unique_number:
                hashmap[a] += 1
            else:
                hashmap[a] = 1

        solution = set()
        for i, h in enumerate(hashmap):
            solution.add(hashmap[h])

        return True if len(solution) == len(hashmap) else False