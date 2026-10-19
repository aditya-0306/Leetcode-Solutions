

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
            
        p_count = [0] * 26
        s_count = [0] * 26
        
        for char in p:
            p_count[ord(char) - ord('a')] += 1
            
        res = []
        p_len = len(p)
        
        for i in range(len(s)):
            # Add current character to window
            s_count[ord(s[i]) - ord('a')] += 1
            
            # Remove character falling out of the window left side
            if i >= p_len:
                s_count[ord(s[i - p_len]) - ord('a')] -= 1
                
            # Compare frequency counts
            if s_count == p_count:
                res.append(i - p_len + 1)
                
        return res
        