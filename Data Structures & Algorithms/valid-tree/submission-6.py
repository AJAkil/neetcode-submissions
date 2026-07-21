from collections import deque
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
        
        def bfs(root, parent):
            Q = deque([(root, parent)])
            visited.add(root)

            while len(Q) > 0:
                node, parent = Q.popleft()
                for nei in get_nei(node):
                    if nei == parent:
                        continue 
                    if nei in visited:
                        return False
                    
                    visited.add(nei)
                    Q.append((nei, node))
            
            return len(visited) == n
    
        def dfs(node, parent):
            # base case 
            if node in visited:
                return False

            visited.add(node)

            #print(node,'-',parent)
            for nei in get_nei(node):
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            

            return True

        #return dfs(0, -1) and len(visited) == n
        return bfs(0, -1)

        