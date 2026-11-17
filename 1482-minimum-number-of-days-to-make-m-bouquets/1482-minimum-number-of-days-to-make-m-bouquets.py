
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
            
        def can_make_bouquets(days):
            bouquets = 0
            flowers = 0
            for d in bloomDay:
                if d <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        low, high = min(bloomDay), max(bloomDay)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_make_bouquets(mid):
                ans = mid
                high = mid - 1  # Try finding an earlier valid day
            else:
                low = mid + 1   # Need more time
                
        return ans
        