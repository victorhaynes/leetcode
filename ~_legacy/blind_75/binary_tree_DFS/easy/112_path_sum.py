from typing import Optional, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, current_sum):
            if not node:
                return False
            
            current_sum += node.val
            if not node.left and not node.right:
                return current_sum == targetSum

            left_found = dfs(node.left, current_sum)
            right_found = dfs(node.right, current_sum)

            if left_found:
                return True
            if right_found:
                return True
            return False

        return dfs(root, 0)