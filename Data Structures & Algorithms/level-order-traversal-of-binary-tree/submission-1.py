# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(u, depth):
            if not u:
                return None
            

            # now the q is how do i dynamically update res here,       
            if depth - 1 == len(res):
                res.append([]) # create a new empty

            res[depth-1].append(u.val)
            dfs(u.left, depth+1)
            dfs(u.right, depth+1)

            return
    
        dfs(root,1)
        return res

        