

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        low, high = 1, min(time) * totalTrips
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            trips_made = sum(mid // t for t in time)
            
            if trips_made >= totalTrips:
                ans = mid
                high = mid - 1  # Try finding a smaller valid time
            else:
                low = mid + 1   # Need more time
                
        return ans
        