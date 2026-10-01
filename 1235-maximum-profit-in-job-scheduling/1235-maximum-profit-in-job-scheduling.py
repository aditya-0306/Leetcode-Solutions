

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        
        # dp stores (end_time, max_profit)
        dp = [(0, 0)]
        
        for start, end, prof in jobs:
            # Find the latest job that ends <= current start time
            idx = bisect.bisect_right(dp, (start, float('inf'))) - 1
            prev_profit = dp[idx][1]
            
            curr_profit = prev_profit + prof
            if curr_profit > dp[-1][1]:
                dp.append((end, curr_profit))
                
        return dp[-1][1]
        