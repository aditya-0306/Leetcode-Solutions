
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, dist in roads:
            adj[u].append((v, dist))
            adj[v].append((u, dist))
            
        visited = set()
        queue = deque([1])
        visited.add(1)
        min_score = float('inf')
        
        while queue:
            curr = queue.popleft()
            for neighbor, dist in adj[curr]:
                min_score = min(min_score, dist)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score
        