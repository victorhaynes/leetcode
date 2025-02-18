from typing import Optional, TreeNode

# Time O(n) -> n nodes
# Space O(h) -> height, or O(logn) if balanced

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        is_mirror = True

        def dfs(left_node, right_node):
            nonlocal is_mirror

            if not is_mirror: # flag case
                return
            if not left_node and not right_node: # base case
                return
            if not left_node and right_node:
                is_mirror = False
                return
            if not right_node and left_node:
                is_mirror = False
                return
            if left_node.val != right_node.val:
                is_mirror = False
                return

            dfs(left_node.left, right_node.right)
            dfs(left_node.right, right_node.left)


        dfs(root, root)
        return is_mirror