# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res 

            if not root:
                return 0

            l_val = dfs(root.left)
            r_val = dfs(root.right)

            res = max(res, l_val + r_val)

            
            return 1 + max(l_val, r_val)

        dfs(root)

        return res 

        



        