class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # First, we form the adjacency list
        adj = {i: [] for i in range(numCourses)}
        visited = set()
        done = set()
        orders = []

        for course, pre in prerequisites:
            adj[course].append(pre)

        def dfs(course):
            if course in visited:
                return False

            # if we are at end of the chain with no more prereq
            if adj[course] == []:
                if course not in done:
                    orders.append(course)
                    done.add(course)
                return True # still valid

            visited.add(course)

            for pre in adj[course]:
                # visit the prerequisites of this course
                if not dfs(pre):
                    return False # chain detected

            # else the course is valid to take now
            if course not in done:
                orders.append(course) # set so duplicates wont create issues
                done.add(course)
            # the undoing of the visited set as this needs to bre freshly made each chain
            visited.remove(course)
            adj[course] = [] # we reset this, so shared path in graph dont gets revisited again, and hence, this course and whatever down the path is always valid so we can always take this course

            return True

        for course in range(numCourses):
            if course not in done:
                if not dfs(course):
                    return []

        return orders
