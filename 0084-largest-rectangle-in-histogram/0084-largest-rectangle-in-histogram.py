

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # stores indices
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))
            
        # Clean up remaining bars in the stack
        n = len(heights)
        for idx, height in stack:
            max_area = max(max_area, height * (n - idx))
            
        return max_area
        