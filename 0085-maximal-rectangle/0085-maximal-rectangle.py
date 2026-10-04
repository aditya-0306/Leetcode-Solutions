

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0
        
        def largestRectangleArea(heights: List[int]) -> int:
            stack = []
            max_h_area = 0
            extended_heights = heights + [0]
            
            for i, h in enumerate(extended_heights):
                while stack and extended_heights[stack[-1]] > h:
                    height = extended_heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_h_area = max(max_h_area, height * width)
                stack.append(i)
            return max_h_area
            
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, largestRectangleArea(heights))
            
        return max_area
        