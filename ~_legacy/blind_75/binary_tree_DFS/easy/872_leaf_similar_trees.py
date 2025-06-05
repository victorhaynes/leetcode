# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time O(N+M) - running DFS on size N and M
# Space O(N+M) - the end of a b-tree is N/2 -> N and M/2 -> M

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Thoughts: use DFS because we care about the end of the tree(s)
        def dfs(root, leaf):
            if not root: # base case
                return
            if not root.left and not root.right: # processing case - do something but don't go further down the tree
                leaf.append(root.val)
                return
            # recursive case
            dfs(root.left, leaf)
            dfs(root.right, leaf)


        leaf1 = []
        leaf2 = []
        dfs(root1, leaf1) # for tree one
        dfs(root2, leaf2) # for tree two

        return True if leaf1 == leaf2 else False