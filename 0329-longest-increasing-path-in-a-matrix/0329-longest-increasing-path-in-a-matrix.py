

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]
        
        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]
                
            max_len = 1
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
                    
            memo[r][c] = max_len
            return max_len
            
        global_max = 0
        for r in range(rows):
            for c in range(cols):
                global_max = max(global_max, dfs(r, c))
                
        return global_max
        