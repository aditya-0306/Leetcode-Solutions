

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            grid[r][c] = 0  # Mark as visited / sink the land
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # 1. Sink all land connected to the borders
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 1:
                    dfs(r, c)
                    
        # 2. Count remaining land cells (enclaves)
        enclaves = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    enclaves += 1
                    
        return enclaves
        