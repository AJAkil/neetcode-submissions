# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, seen_max):
            nonlocal res
            # seen_max is the so far max valued node we have seen
            if not root:
                return
            
            temp = 0
            temp = max(root.val, seen_max)

            if root.val >= seen_max:
                res += 1 # only when so far seen is higher or equal than curr node   
            dfs(root.left, temp)
            dfs(root.right, temp)


        dfs(root, root.val)

        return res
        