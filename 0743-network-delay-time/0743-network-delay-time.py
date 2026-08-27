import collections
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build directed adjacency list: u -> list of (weight, neighbor)
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))

        # Min-Heap stores tuples of (time_to_reach_node, node)
        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue

            visited.add(n1)
            max_time = max(max_time, w1)

            # If all nodes have received the signal, return maximum delay
            if len(visited) == n:
                return max_time

            for w2, n2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))

        # If we exit the loop without visiting all n nodes
        return max_time if len(visited) == n else -1
        