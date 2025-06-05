from typing import Optional, List
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time O(n) -> n number of nodes
# Space O(n) -> n is max number of nodes at any level which could be the entire tree worst case

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        solution = []

        queue = collections.deque()
        queue.append(root)

        while queue: # remember the queue can contain null nodes, no guarantee that the nth node is real
            level_sum = 0
            num_real_nodes = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_sum += node.val
                    queue.append(node.left)
                    queue.append(node.right)
                    num_real_nodes += 1

            
            if num_real_nodes: # you need to count the real (non-null) nodes so the math works (sum / count)
                solution.append(level_sum / num_real_nodes)

        return solution
                    