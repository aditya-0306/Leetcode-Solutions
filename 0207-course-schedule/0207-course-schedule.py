class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
            
        # 0 = Unvisited, 1 = Visiting (in current path), 2 = Visited
        state = [0] * numCourses
        
        def has_cycle(course):
            if state[course] == 1:  # Found cycle
                return True
            if state[course] == 2:  # Already verified safe
                return False
                
            state[course] = 1  # Mark as visiting
            for neighbor in adj[course]:
                if has_cycle(neighbor):
                    return True
            state[course] = 2  # Mark as visited
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False
                
        return True
        