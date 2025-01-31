from typing import Optional, TreeNode
# Time O(n)
# Space O(n) or O(logn) if the tree is balanced

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # DFS - RECURSION (in-order)
        # # DFS - RECURSION (in-order)
        # # DFS - RECURSION (in-order)
        # # Base Case: if the current node (root) is empty, return 0 depth
        if not root:
            return 0

        # Else - Recursive case:
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)

        # # DFS - ITERATIVE (pre-ordered)
        # # DFS - ITERATIVE (pre-ordered)
        # # DFS - ITERATIVE (pre-ordered)
        # if not root:
        #     return 0

        # stack = [[root, 1]]
        # result = 1
        # while stack:
        #     node, depth = stack.pop()
        #     if node:
        #         result = max(result, depth)
        #         stack.append([node.left, depth + 1]) # may/can add null nodes. If it is null the above if will prevent work
        #         stack.append([node.right, depth + 1])

        # return result


        # # BFS - "level order traversal" - uses a dequeue normally
        # # BFS - "level order traversal" - uses a dequeue normally
        # # BFS - "level order traversal" - uses a dequeue normally
        # # logic: add the root to a queue then replace it with it's children 
        # if not root:
        #     return 0

        # level = 0
        # queue = deque([root])
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     level += 1

        # return level