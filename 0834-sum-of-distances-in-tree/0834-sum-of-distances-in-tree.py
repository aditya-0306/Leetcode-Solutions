

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        count = [1] * n
        res = [0] * n
        
        def dfs_post(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs_post(neighbor, node)
                    count[node] += count[neighbor]
                    res[0] += res[neighbor] + count[neighbor]
                    
        def dfs_pre(node, parent):
            for neighbor in graph[node]:
                if neighbor != parent:
                    # Re-rooting formula
                    res[neighbor] = res[node] - count[neighbor] + (n - count[neighbor])
                    dfs_pre(neighbor, node)
                    
        dfs_post(0, -1)
        dfs_pre(0, -1)
        return res
        