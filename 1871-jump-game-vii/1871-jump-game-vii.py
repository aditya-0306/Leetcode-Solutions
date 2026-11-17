class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False
            
        dp = [False] * n
        dp[0] = True
        reachable_count = 0
        
        for i in range(1, n):
            if i >= minJump:
                reachable_count += dp[i - minJump]
            if i > maxJump:
                reachable_count -= dp[i - maxJump - 1]
                
            if reachable_count > 0 and s[i] == '0':
                dp[i] = True
                
        return dp[-1]
        