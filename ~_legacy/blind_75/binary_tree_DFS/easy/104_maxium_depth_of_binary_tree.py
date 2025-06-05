from typing import Optional, TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # if no tree, depth is 0 don't check anything
            return 0


        max_depth = 1

        def dfs(node, current_depth):
            nonlocal max_depth

            if not node: # base case
                return

            if node.left or node.right:
                current_depth += 1
                max_depth = max(current_depth, max_depth)

            dfs(node.left, current_depth)
            dfs(node.right, current_depth)


        dfs(root, 1)
        return max_depth