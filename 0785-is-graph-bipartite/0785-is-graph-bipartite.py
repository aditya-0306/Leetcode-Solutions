

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}  # Map node to color (0 or 1)
        
        for i in range(len(graph)):
            if i not in color:
                queue = deque([i])
                color[i] = 0
                
                while queue:
                    node = queue.popleft()
                    
                    for neighbor in graph[node]:
                        if neighbor in color:
                            if color[neighbor] == color[node]:
                                return False
                        else:
                        # Color neighbor with the opposite color
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                            
        return True