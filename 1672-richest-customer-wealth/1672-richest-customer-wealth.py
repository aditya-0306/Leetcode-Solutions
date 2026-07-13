class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for accounts in accounts:
            if sum(accounts) > max_wealth:
                max_wealth = sum(accounts)

        return max_wealth
        