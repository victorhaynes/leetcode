from typing import TreeNode

# Time O(n) -> all nodes need visiting
# Space O(h) -> best case O(logn) if the tree is symmetrical (always the max depth of the recursion stack)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node, max_val):
            if not node:
                return # end the call and go back up the recursion stack
            
            if node.val >= max_val:
                self.count += 1
                max_val = node.val

            # Recur for left and right, they will stop when a null node is reached
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        
        dfs(root, root.val) # the maximum is the root node's value/1st node so far
        return self.count