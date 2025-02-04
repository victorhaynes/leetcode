from typing import Optional, TreeNode

# Time O(n)
# Space O(n) - O(logn) if symmetrical

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(node1, node2):
            # Base Case(s) - stop conditions including edge cases
            if not node1 and not node2:
                return True # both empty == they are identical
            if node1 and not node2: # one is empty
                return False
            if node2 and not node1: # the other is empty
                return False
            if node1.val != node2.val: # if the values aren't equal, main condition
                return False

            left_subtree = dfs(node1.left, node2.left)
            right_subtree = dfs(node1.right, node2.right)

            return (left_subtree and right_subtree)

        return dfs(p, q)


            