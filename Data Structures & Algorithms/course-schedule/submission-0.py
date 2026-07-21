class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()

        # form the adj list first
        prereq = {i: [] for i in range(numCourses)}

        for course, p in prerequisites:
            prereq[course].append(p) # cause a course may have many prereq

        def dfs(course):
            # return T/F

            # base case
            if course in visited:
                # we detected a cycle, so we return false
                return False
            
            if prereq[course] == []:
                # we hit a course that doesnt have a prerq - so its the end of the chain
                # we return True
                return True
            
            # add the current course to the visited set
            visited.add(course)
            
            # else we go through the prereq of the current course:
            for pre in prereq[course]:
                # if we find that the dfs from the pre req returned false, there is a loop
                # so we return False immedietly
                if not dfs(pre):
                    return False
            
            # if we reach here, it means, we succesfully traversed through the prereq
            # chain and didnt hit any false, so we must have hit true, and so
            # must have found a course without any cycles

            # Since we found that the current course can clearly be taken, we clear it up
            # from the visited set
            visited.remove(course)

            # and since the current course can be taken, so we can safely set the prereq to be 
            # empty list, so that we dont have to traverse the rest of the chain from here
            prereq[course] = []

            return True




        # conduct dfs from each courses
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        