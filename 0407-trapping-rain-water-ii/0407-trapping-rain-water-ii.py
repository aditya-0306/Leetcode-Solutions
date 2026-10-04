

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
            
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
            
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        
        # Step 1: Push all boundary cells into the min-heap
        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    heapq.heappush(min_heap, (heightMap[r][c], r, c))
                    visited[r][c] = True
                    
        water_trapped = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Step 2: Expand inward using BFS with a min-heap
        while min_heap:
            h, r, c = heapq.heappop(min_heap)
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    water_trapped += max(0, h - heightMap[nr][nc])
                    # Push max height to propagate the bottleneck constraint
                    heapq.heappush(min_heap, (max(heightMap[nr][nc], h), nr, nc))
                    
        return water_trapped
        