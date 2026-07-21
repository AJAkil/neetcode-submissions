class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        order = []
        prereq = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            prereq[course].append(pre)

        def dfs(course):
            if course in visited:
                return False
            
            if prereq[course] == []:
                return True
            
            visited.add(course)

            # get the prereq:
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            
            # we are here - so we can take the current course
            order.append(course)
            visited.remove(course) # we remove the current course from the visited array
            prereq[course] = [] # a little optimization, so that we dont repeat work again

            return True

        # add the ones to the output without any dependency first
        for course in prereq:
            if prereq[course] == []:
                order.append(course)
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order
            

        