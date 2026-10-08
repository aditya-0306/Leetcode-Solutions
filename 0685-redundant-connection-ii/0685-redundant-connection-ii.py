

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {}
        candidate1 = None
        candidate2 = None
        
        # Step 1: Check if any node has two parents
        for u, v in edges:
            if v in parent:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
                break
            parent[v] = u
            
        # Step 2: Union-Find to detect cycles
        uf = list(range(n + 1))
        
        def find(i):
            if uf[i] != i:
                uf[i] = find(uf[i])
            return uf[i]
            
        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i == root_j:
                return False
            uf[root_j] = root_i
            return True
            
        for u, v in edges:
            # If candidate2 exists, skip it to check if a cycle forms without it
            if [u, v] == candidate2:
                continue
            
            if not union(u, v):
                # Cycle found!
                if candidate1:
                    # If there's a node with two parents, candidate1 is the correct edge to remove
                    return candidate1
                return [u, v]
                
        # If no cycle was found when skipping candidate2, then candidate2 is the culprit
        return candidate2
        