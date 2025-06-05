from typing import Optional, TreeNode

# Time O(n) -> n number of nodes
# Space O(h) -> height of tree/max recurssion depth, O(logn) in the best case of a balanced tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        found = False

        def dfs(node, curr_sum):
            nonlocal found

            if not node or found: # base case, and flag case
                return

            curr_sum += node.val
            if curr_sum == targetSum:
                found = True
                return

            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
        dfs(root, 0)

        return found

