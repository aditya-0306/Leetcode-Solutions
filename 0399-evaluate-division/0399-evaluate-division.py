

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
            
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
                
            queue = deque([(start, 1.0)])
            visited = {start}
            
            while queue:
                curr, prod = queue.popleft()
                if curr == end:
                    return prod
                    
                for neighbor, weight in graph[curr].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, prod * weight))
                        
            return -1.0
            
        return [bfs(q[0], q[1]) for q in queries]
        