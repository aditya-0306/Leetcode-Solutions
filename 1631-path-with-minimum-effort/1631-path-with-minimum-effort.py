

class Solution:
    def minimumEffortPath(self, heights: List[List[str]]) -> int:
        rows, cols = len(heights), len(heights[0])
        # Min-heap stores (effort, r, c)
        min_heap = [(0, 0, 0)]
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while min_heap:
            current_effort, r, c = heapq.heappop(min_heap)
            
            # If we reached the bottom-right corner, return the effort
            if r == rows - 1 and c == cols - 1:
                return current_effort
                
            # If we found a heavier path already, skip
            if current_effort > efforts[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(current_effort, abs(heights[nr][nc] - heights[r][c]))
                    
                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))
                        
        return 0
        