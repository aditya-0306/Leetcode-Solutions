

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
            
        max_points = 1
        
        for i in range(n):
            slopes = {}
            duplicates = 0
            curr_max = 0
            
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                    continue
                    
                dx = x2 - x1
                dy = y2 - y1
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                
                # Normalize signs for consistency
                if dx < 0:
                    dx, dy = -dx, -dy
                elif dx == 0:
                    dy = abs(dy)
                
                slope = (dx, dy)
                slopes[slope] = slopes.get(slope, 0) + 1
                curr_max = max(curr_max, slopes[slope])
                
            max_points = max(max_points, curr_max + duplicates + 1)
            
        return max_points
        