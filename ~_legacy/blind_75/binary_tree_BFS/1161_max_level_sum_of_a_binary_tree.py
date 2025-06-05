from collections import deque
from typing import Optional

# time O(n) -> n nodes
# Soace O(n) -> queue of size n/2 (in worst case, last row of a balanced tree) and hash_map of size n in worst case , n + n = n

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float("-inf")

        queue = deque()
        queue.append(root)
        hash_map = {}

        level = 1
        while queue:
            
            curr_sum = 0
            non_zero_nodes = 0 # if you have a level of no nodes don't add anything to our hashmap

            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    curr_sum += node.val
                    non_zero_nodes += 1

            if non_zero_nodes:
                max_sum = max(max_sum, curr_sum)

                if hash_map.get(max_sum):
                    pass
                else:
                    hash_map[max_sum] = level

            level += 1

        return hash_map[max_sum]