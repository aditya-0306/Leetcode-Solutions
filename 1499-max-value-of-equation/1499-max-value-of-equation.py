

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dq = deque() # Stores pairs of (y - x, x)
        max_val = float('-inf')
        
        for x, y in points:
            # Remove points outside the x window k
            while dq and x - dq[0][1] > k:
                dq.popleft()
                
            # If deque has valid elements, calculate equation value using the max term from front
            if dq:
                max_val = max(max_val, dq[0][0] + y + x)
                
            # Maintain monotonic decreasing property for (y - x)
            curr_val = y - x
            while dq and dq[-1][0] <= curr_val:
                dq.pop()
                
            dq.append((curr_val, x))
            
        return max_val
        