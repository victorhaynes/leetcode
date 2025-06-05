# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time O(h) -> the height of the tree for a binary search tree find operation, we travel the height at most -> h = logn in balanced tree, worst case h = n unbalanced tree
# Space O(1) no extra memory used

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # Binary Search Tree: Each node is greater than every node in its left subtree
        # each node is less than every node in its right subtree

        # Operations: Insert, Find, Delete

        # Insert:
        # start a root, always insert as a leaf

        # Find:
        # Compare desired vs current and go left or right

        # Delete:
        # three cases... 1) leaf 2) one child 3) two children

        node = root
        while node:
            if val < node.val:
                node = node.left
            elif val > node.val:
                node = node.right
            else:
                return node

        return None