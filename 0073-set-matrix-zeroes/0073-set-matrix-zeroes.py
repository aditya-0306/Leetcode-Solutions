

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_col_zero = False
        
        # Step 1: Mark zeroes in the first row and column
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    
        # Step 2: Use markers to set elements to zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                    
        # Step 3: Zero out the first row if needed
        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0
                
        # Step 4: Zero out the first column if needed
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
        