class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize DP array with amount + 1 as placeholder
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0
        
        # Build solution for each sub-amount
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        # If dp[amount] was never updated, amount cannot be formed
        return dp[amount] if dp[amount] != amount + 1 else -1
        