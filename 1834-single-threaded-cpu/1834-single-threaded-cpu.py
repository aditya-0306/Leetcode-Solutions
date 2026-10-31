

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Append original index to each task, then sort by enqueue time
        indexed_tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        
        res = []
        min_heap = [] # Stores (processing_time, index)
        i = 0
        n = len(tasks)
        current_time = 0
        
        while i < n or min_heap:
            # If heap is empty, jump time to the next available task's enqueue time
            if not min_heap and current_time < indexed_tasks[i][0]:
                current_time = indexed_tasks[i][0]
                
            # Push all tasks that have arrived by current_time into the heap
            while i < n and indexed_tasks[i][0] <= current_time:
                _, proc_time, original_idx = indexed_tasks[i]
                heapq.heappush(min_heap, (proc_time, original_idx))
                i += 1
                
            # Execute the optimal task
            proc_time, original_idx = heapq.heappop(min_heap)
            current_time += proc_time
            res.append(original_idx)
            
        return res
        