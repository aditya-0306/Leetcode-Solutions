class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> list[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        