

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Pair nums2 and nums1, sort in descending order of nums2
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        min_heap = []
        current_sum = 0
        max_score = 0
        
        for n2, n1 in pairs:
            heapq.heappush(min_heap, n1)
            current_sum += n1
            
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
                
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * n2)
                
        return max_score
        