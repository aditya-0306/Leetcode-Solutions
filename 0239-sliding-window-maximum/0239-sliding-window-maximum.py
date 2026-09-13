

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # stores indices
        left = right = 0
        
        while right < len(nums):
            # Pop smaller values from the back of the deque
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            
            # Remove left index if it's outside the current window
            if left > q[0]:
                q.popleft()
                
            # If window size has reached k, record result and advance left pointer
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
            right += 1
            
        return output
        