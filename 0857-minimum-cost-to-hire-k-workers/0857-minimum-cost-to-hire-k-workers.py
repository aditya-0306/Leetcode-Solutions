

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Pair workers by (ratio, quality, wage)
        workers = sorted([(w / q, q, w) for q, w in zip(quality, wage)])
        
        min_cost = float('inf')
        max_heap = [] # stores negative qualities to act as a max-heap
        sum_quality = 0
        
        for ratio, q, w in workers:
            heapq.heappush(max_heap, -q)
            sum_quality += q
            
            if len(max_heap) > k:
                # Remove the worker with the largest quality
                sum_quality += heapq.heappop(max_heap)
                
            if len(max_heap) == k:
                min_cost = min(min_cost, sum_quality * ratio)
                
        return min_cost
        