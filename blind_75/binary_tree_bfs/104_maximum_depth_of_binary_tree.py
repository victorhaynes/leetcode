from collections import deque
from typing import Optional

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n) -> must visit all nodes
# space: O(h) -> height of tree O(n) unbalanced tree or O(logn) in balanced tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0 # no levels


        queue = deque()
        queue.append(root)

        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            level +=1

        return level 