

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])  # Path compression
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            
            if root_i == root_j:
                return False  # Cycle detected
            parent[root_i] = root_j
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
                
        return []
        