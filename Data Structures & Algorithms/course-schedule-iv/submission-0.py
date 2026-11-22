class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}

        for pre, course in prerequisites:
            adj[course].append(pre)
        
        print(adj)

        answer = [False for _ in range(len(queries))]
        reach = {i: set() for i in range(numCourses)}
        done = set()

        def dfs(course):
            if course in done:
                return reach[course]

            for pre in adj[course]:
                reach[course].add(pre)
                reach[course] |= dfs(pre)
            
            done.add(course)
            return reach[course]

        # filling the reachability map here
        for course in range(numCourses):
            dfs(course)
        print(reach)


        for i,q in enumerate(queries):
            # check if u is a prereq of v or not
            u,v = q[0], q[1]
            if u in reach[v]:
                answer[i] = True

        return answer

