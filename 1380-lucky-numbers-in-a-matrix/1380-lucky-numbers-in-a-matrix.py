class Solution:
    def luckyNumbers(self, matrix):
        row_min = {min(row) for row in matrix}

        col_max = set()

        for j in range(len(matrix[0])):
            maximum = matrix[0][j]

            for i in range(1, len(matrix)):
                maximum = max(maximum, matrix[i][j])

            col_max.add(maximum)

        return list(row_min & col_max)