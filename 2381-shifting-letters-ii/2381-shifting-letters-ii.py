

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        
        # Populate difference array
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            diff[end + 1] -= val
            
        # Compute prefix sums to get net shift for each index
        res = []
        current_shift = 0
        for i in range(n):
            current_shift += diff[i]
            # Normalize shift within 0-25 range handling negative values
            net_shift = (ord(s[i]) - ord('a') + current_shift) % 26
            res.append(chr(ord('a') + net_shift))
            
        return "".join(res)
        