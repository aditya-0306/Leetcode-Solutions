class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        for i in range(len(s)):
            # Odd length palindromes (center is i)
            count += self.expand(s, i, i)
            # Even length palindromes (center is between i and i+1)
            count += self.expand(s, i, i + 1)
            
        return count
        
    def expand(self, s: str, left: int, right: int) -> int:
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res
        