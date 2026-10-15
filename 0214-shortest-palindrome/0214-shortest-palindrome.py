class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
            
        # Combine s, a separator, and the reverse of s
        rev_s = s[::-1]
        combined = s + "#" + rev_s
        
        # Build KMP LPS (Longest Prefix Suffix) array
        lps = [0] * len(combined)
        j = 0
        for i in range(1, len(combined)):
            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]
            if combined[i] == combined[j]:
                j += 1
                lps[i] = j
                
        # Length of the longest palindromic prefix
        palindrome_len = lps[-1]
        
        # Prepend the reverse of the remaining suffix to s
        to_add = rev_s[:len(s) - palindrome_len]
        return to_add + s
        