

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max-heap using negative distances
        heap = []
        
        for x, y in points:
            dist = -(x**2 + y**2)
            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            else:
                if dist > heap[0][0]:
                    heapq.heappushpop(heap, (dist, x, y))
                    
        return [[x, y] for (dist, x, y) in heap]
        