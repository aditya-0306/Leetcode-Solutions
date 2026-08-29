class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # If the sum is odd, we cannot partition into two equal subsets
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # dp[i] will store whether a subset sum of `i` is possible
        dp = [False] * (target + 1)
        dp[0] = True  # A sum of 0 is always achievable (empty set)
        
        for num in nums:
            # Iterate backwards so we use each element at most once per pass
            for curr_sum in range(target, num - 1, -1):
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - num]
                
            # Early exit if we already found a valid subset
            if dp[target]:
                return True
                
        return dp[target]
        