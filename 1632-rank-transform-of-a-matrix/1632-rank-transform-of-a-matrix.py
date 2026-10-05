

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        val_map = defaultdict(list)
        
        for r in range(m):
            for c in range(n):
                val_map[matrix[r][c]].append((r, c))
                
        rank = [0] * (m + n)
        res = [[0] * n for _ in range(m)]
        
        for val in sorted(val_map.keys()):
            cells = val_map[val]
            
            # Union-Find parent array
            parent = list(range(m + n))
            
            def find(i):
                if parent[i] != i:
                    parent[i] = find(parent[i])
                return parent[i]
            
            def union(i, j):
                root_i, root_j = find(i), find(j)
                if root_i != root_j:
                    parent[root_j] = root_i
                    
            # Connect row and column indices for each cell with the same value
            for r, c in cells:
                union(r, c + m)
                
            # Group cells by their connected component root
            components = defaultdict(list)
            for r, c in cells:
                components[find(r)].append((r, c))
                
            # Calculate ranks for each component
            for root, comp_cells in components.items():
                max_rank = 0
                for r, c in comp_cells:
                    max_rank = max(max_rank, rank[r], rank[c + m])
                
                new_rank = max_rank + 1
                for r, c in comp_cells:
                    rank[r] = rank[c + m] = res[r][c] = new_rank
                    
        return res
        