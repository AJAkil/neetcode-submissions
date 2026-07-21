class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = {i: [] for i in range(n)}


        # create the adjacency list first
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        print(adj)
        
        def get_nei(node):
            return adj[node]
        
        def dfs(node):
            # base case
            if node in visited:
                return 
            
            visited.add(node)
            for nei in get_nei(node):
                dfs(nei)
        
        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        
        return res

        
