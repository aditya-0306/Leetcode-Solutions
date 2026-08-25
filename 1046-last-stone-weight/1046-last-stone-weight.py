import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Negate values to simulate a Max-Heap in Python
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # Keep smashing the two heaviest stones
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)   # Heaviest stone
            second = -heapq.heappop(max_heap)  # Second heaviest stone
            
            if first != second:
                heapq.heappush(max_heap, -(first - second))
                
        # Return remaining stone weight or 0 if heap is empty
        return -max_heap[0] if max_heap else 0