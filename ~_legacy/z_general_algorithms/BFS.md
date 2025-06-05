# General DFS setup - from leetcode 102

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        solution = []

        queue = collections.deque() # 1) Initialize a de/queue, add root to the queue
        queue.append(root)

        while queue: # 2) Initialize while loop, while queue is not empty do work

            level_content = []
            for _ in range(len(queue)): # 3) for _ in range len(queue)L to define the "level" level work
                node = queue.popleft() # 4) popleft the 1st node in the queue
                if node: 
                    level_content.append(node.val)
                    queue.append(node.left) # 5) if it is a valid node add it's children (which can be null)
                    queue.append(node.right)

            if level_content:
                solution.append(level_content)

        return solution
```