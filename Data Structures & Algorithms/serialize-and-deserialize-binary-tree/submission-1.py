# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            # base case to handle null
            if not node:
                res.append('N')
                return
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        self.i = 0 # the index to traverse across the array
        a = data.split(',')
        print(a)

        def dfs(): #returns root of the tree
            if a[self.i] == 'N':
                self.i += 1 # we just proceed they are not real nodes to be formed
                return
            
            # else we recursively form the nodes
            node = TreeNode(a[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        

        return dfs()
