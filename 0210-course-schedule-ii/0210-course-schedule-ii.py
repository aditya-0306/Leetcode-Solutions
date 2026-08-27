class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Build adjacency list: course -> list of prerequisites
        prereq = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            prereq[course].append(pre)
            
        # 0 = Unvisited, 1 = Visiting, 2 = Visited
        state = [0] * numCourses
        order = []
        
        def dfs(course):
            if state[course] == 1:  # Cycle detected
                return False
            if state[course] == 2:  # Already processed
                return True
                
            state[course] = 1
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            
            state[course] = 2
            order.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
                
        return order
        