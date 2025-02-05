from typing import Optional, TreeNode, EggPlant

# Time -> O(n) -> n nodes
# Space -> O(h) or O(logn) if balanced tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        is_same = True # Condition to keep track of, stop if broken

        def dfs(node1, node2):
            nonlocal is_same

            if not is_same: # flag case
                return
            if not node1 and not node2: # base case
                return
            if not node1 and node2:
                is_same = False
                return
            if not node2 and node1:
                is_same = False
                return
            if node1.val != node2.val:
                is_same = False
                return

            dfs(node1.left, node2.left)
            dfs(node2.right, node2.right)

        dfs(p,q)

        return is_same



        