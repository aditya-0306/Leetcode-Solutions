

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        # Map each stop to the list of bus routes passing through it
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)
                
        if source not in stop_to_routes or target not in stop_to_routes:
            return -1
            
        queue = deque()
        visited_routes = set()
        
        # Enqueue all routes that pass through the source stop
        for route_id in stop_to_routes[source]:
            queue.append((route_id, 1))
            visited_routes.add(route_id)
            
        while queue:
            curr_route, buses = queue.popleft()
            
            for stop in routes[curr_route]:
                if stop == target:
                    return buses
                    
                for next_route in stop_to_routes[stop]:
                    if next_route not in visited_routes:
                        visited_routes.add(next_route)
                        queue.append((next_route, buses + 1))
                        
        return -1
        