
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'  # Mark entrance as visited
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c, steps = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == '.':
                    # Check if it's an exit (on the boundary)
                    if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                        return steps + 1
                    
                    maze[nr][nc] = '+'  # Mark as visited
                    queue.append((nr, nc, steps + 1))
                    
        return -1
        