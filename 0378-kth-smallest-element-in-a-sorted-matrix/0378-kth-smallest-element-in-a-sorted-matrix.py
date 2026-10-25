

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]
        
        def count_less_equal(mid):
            count = 0
            r, c = n - 1, 0  # Start from bottom-left
            while r >= 0 and c < n:
                if matrix[r][c] <= mid:
                    count += (r + 1)  # All elements above this column in this row are <= mid
                    c += 1
                else:
                    r -= 1
            return count

        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid
                
        return low
        