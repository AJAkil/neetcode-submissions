# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            l_val = dfs(root.left)
            r_val = dfs(root.right)

            # res = abs(l_val - r_val) <= 1 <- wrong approach
            # because this will override instances of unbalanced and it
            # might make res = True, correct way is to set it to False
            # when we see imbaalnce
            if abs(l_val - r_val) > 1:
                res = False

            

            return 1 + max(l_val, r_val)
        
        dfs(root)

        return res
        