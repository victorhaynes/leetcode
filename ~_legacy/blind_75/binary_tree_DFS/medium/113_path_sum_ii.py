from typing import Optional, List

# Time O(n^2) - skewed, we need N traversials and must copy the path which takes worst case N time or 
# best case time - O(n logn) if the tree is balanced n * h where h == logn
# Space O(

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        solution = []

        def dfs(node, curr_sum, curr_path):
            if not node: # base case, no flag case needed bc we must go through entire tree
                return

            curr_path.append(node.val)
            curr_sum += node.val

            # if we are at a leaf, check the sums
            if not node.left and not node.right and curr_sum == targetSum:
                solution.append(curr_path.copy()) # create a deep copy of path list, do not append a reference of path

            dfs(node.left, curr_sum, curr_path)
            dfs(node.right, curr_sum, curr_path)

            curr_path.pop() # back track, lists are mutable so we must revert the change

        dfs(root,0,[])
        return solution