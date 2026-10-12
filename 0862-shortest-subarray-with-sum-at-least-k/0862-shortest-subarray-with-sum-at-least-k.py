

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        ans = float('inf')
        deque_indices = deque() # Stores indices of prefix sums
        
        for y in range(n + 1):
            # Remove valid starting points from the front
            while deque_indices and prefix[y] - prefix[deque_indices[0]] >= k:
                ans = min(ans, y - deque_indices.popleft())
                
            # Maintain monotonic increasing order in the deque
            while deque_indices and prefix[y] <= prefix[deque_indices[-1]]:
                deque_indices.pop()
                
            deque_indices.append(y)
            
        return ans if ans != float('inf') else -1
        