# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, a,b):
            if not node:
                return True # we reached the end of the DFS

            # Now what if it's invalid? 
            if node.val <= a or node.val >= b:
                return False

            # the recursive step
            return dfs(node.left, a, node.val) and dfs(node.right, node.val, b)

        return dfs(root, float('-inf'), float('+inf'))

        