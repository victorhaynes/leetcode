from typing import List
"""
URL: https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).


Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""

# Optimal
# Time O(n^2) we iterate n times over grid and have to convert a row (list) of size n into a tuple which takes O(n) time n times == O(n^2)
# Space O(n^2) we store n number of rows as a dict key but we have to convert the size n key to a tuple of size n == n^2
# hard problem to me
# remember zip() iterates 2 or more iterables of the same length ([1,2,3], [4,5,6]) -> i0 = (1,4) -> i1 = (2,5) -> i2 = (3,6)
# the element in the for _ in zip() loop is a tuple of the arguments passed in
# remember unpack operator * unpacks the list of lists into individual elements
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        row_counts = {}
        pairs = 0
        
        for row in grid:
            if row_counts.get(tuple(row)):
                row_counts[tuple(row)] += 1
            else:
                row_counts[tuple(row)] = 1

        for column in zip(*grid):
            if row_counts.get(column):
                pairs += row_counts[column]

        return pairs