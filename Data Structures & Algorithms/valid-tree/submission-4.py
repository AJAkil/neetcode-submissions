class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def get_nei(node):
            return adj[node]

        visited = set()

        # tree case
        if len(edges) > n-1:
            return False 
    
        def dfs(node, parent):
            #print(node,'-',parent)
            for nei in get_nei(node):
                if nei in visited and nei != parent:
                    return False 
                if nei == parent:
                    continue
                visited.add(nei)
                dfs(nei, node)
            

            return True

        visited.add(0)
        return dfs(0, -1) and len(visited) == n

        