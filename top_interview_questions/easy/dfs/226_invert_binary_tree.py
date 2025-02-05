from typing import Optional, TreeNode

# Time O(n) -> n nodes
# Space O(h) -> h is the height of the tree, or O(logn) if balanced tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # no flag needed for this problem

        def dfs(node):

            if not node:
                return

            temp = node.left
            node.left = node.right
            node.right = temp

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return root