

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = [] # stores negative fuel values to act as a max-heap
        stations.append([target, 0]) # Sentinel to process the final distance to target
        
        curr_fuel = startFuel
        prev_pos = 0
        stops = 0
        
        for pos, fuel in stations:
            # Consume fuel needed to travel from previous position to current station
            curr_fuel -= (pos - prev_pos)
            
            # If we run out of gas, greedily refuel from the best past station
            while curr_fuel < 0 and max_heap:
                curr_fuel += -heapq.heappop(max_heap)
                stops += 1
                
            # If we still can't reach this position, it's unreachable
            if curr_fuel < 0:
                return -1
                
            # Save this station's fuel for potential future use
            heapq.heappush(max_heap, -fuel)
            prev_pos = pos
            
        return stops
        