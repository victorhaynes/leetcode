from typing import List
# Time O(mxn)
# space O(mxn)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0


        num_rows, num_cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(i,j):
            if i < 0 or i >= num_rows or j < 0 or j >= num_cols or grid[i][j] != '1': # Base case, basically be in bounds + any problem specifics. In this case if it is a not a "1" return
                return
            else: # only do work in the non-base case. RIGHT DOWN LEFT UP is standard for DFS graph .... j + 1 -> i + 1 -> j -1  -> i - 1
                grid[i][j] = '0'
                dfs(i, j + 1) # right
                dfs(i + 1, j) # down
                dfs(i, j - 1) # left
                dfs(i - 1, j) # up

        for i in range(num_rows): # vertical movement
            for j in range(num_cols): # horizontal movement
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i,j)       
                    # remember this function is actually modifying the grid so the next time we see a 1 it will be valid to count
                    # the RECURSIVE calls inside the original call are what are removing the 1s!!!!!!


        return num_islands



