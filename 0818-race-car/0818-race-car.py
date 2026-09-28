

class Solution:
    def racecar(self, target: int) -> int:
        # Queue stores (position, speed, steps)
        queue = deque([(0, 1, 0)])
        visited = {(0, 1)}
        
        while queue:
            pos, speed, steps = queue.popleft()
            
            if pos == target:
                return steps
                
            # Choice 1: Accelerate ('A')
            next_pos = pos + speed
            next_speed = speed * 2
            if (next_pos, next_speed) not in visited and abs(next_pos - target) < target:
                visited.add((next_pos, next_speed))
                queue.append((next_pos, next_speed, steps + 1))
                
            # Choice 2: Reverse ('R')
            reverse_speed = -1 if speed > 0 else 1
            if (pos, reverse_speed) not in visited and abs(pos - target) < target:
                visited.add((pos, reverse_speed))
                queue.append((pos, reverse_speed, steps + 1))
                
        return -1
        