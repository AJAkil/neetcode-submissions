class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(u, parent):
            
            # first we check if we already visited this node
            if u in visit:
                return True # that means its a cycle -> done!
            
            visit.add(u) # else we add this node to the temp visited list

            for v in adj[u]:
                if v == parent:
                    continue # we skip the parent
                
                # else we do dfs
                if dfs(v, u): # from the parent
                    return True
            
            return False # if we dont have any true we return false
        
        # we need an adj list formulation from the list
        # but the trick is we need to process each edge as we
        # proceed because we need the latest edge that creates the
        # cycle, so we do not form the entire graph first and then
        # we proceed the cycle, we add an edge, and we process with dfs 
        # from that edge, and eventually if that is the one creating issue
        # we got the answer!!

        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            # everytime we start the dfs pass we make a fresh set.
            # because if we don't we will wrongly mark the nodes we
            # saw in last iteration, cause new edge makes a new G instance
            visit = set()

            if dfs(u,-1): # if dfs is true, that means this new edge we are considering is the cause of cycle, and by default its the latest one in the list of edges
                return [u,v]

        # what if there is no cycle at all? we return empty list?
        return []

