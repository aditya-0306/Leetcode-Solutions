

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_sizes = {}
        island_id = 2
        
        def dfs(r, c, identifier):
            if not (0 <= r < n and 0 <= c < n) or grid[r][c] != 1:
                return 0
            grid[r][c] = identifier
            size = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                size += dfs(r + dr, c + dc, identifier)
            return size

        # Step 1: Color each island and record its size
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1
                    
        max_size = max(island_sizes.values(), default=0)
        
        # Step 2: Evaluate flipping each 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                            
                    current_total = 1 + sum(island_sizes[i] for i in seen)
                    max_size = max(max_size, current_total)
                    
        return max_size
        