

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        dict_t = Counter(t)
        required = len(dict_t)
        
        formed = 0
        window_counts = {}
        
        # ans tuple: (window length, left, right)
        ans = float("inf"), None, None
        l, r = 0, 0
        
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
                
            while l <= r and formed == required:
                character = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                    
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                    
                l += 1
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
        