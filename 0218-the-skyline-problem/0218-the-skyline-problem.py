
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for L, R, H in buildings:
            # Start event: negative height so it processes first among same X
            events.append((L, -H, R))
            # End event: positive height
            events.append((R, H, L))
            
        # Sort events: primary by x, secondary by height descriptor
        events.sort()
        
        res = [[0, 0]]
        live = [0]
        lazy_deleted = {}
        
        for x, h_desc, r_val in events:
            if h_desc < 0:
                # Start event: height is -h_desc
                h = -h_desc
                heapq.heappush(live, -h)
            else:
                # End event: height is h_desc
                h = h_desc
                lazy_deleted[h] = lazy_deleted.get(h, 0) + 1
                
            # Clean up the top of the heap from lazy-deleted elements
            while live and -live[0] in lazy_deleted:
                top_h = -live[0]
                lazy_deleted[top_h] -= 1
                if lazy_deleted[top_h] == 0:
                    del lazy_deleted[top_h]
                heapq.heappop(live)
                
            current_max = -live[0]
            if res[-1][1] != current_max:
                res.append([x, current_max])
                
        return res[1:]