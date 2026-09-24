

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        if not s:
            return [""]
            
        queue = deque([s])
        visited = {s}
        found = False
        level_results = set()
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                curr = queue.popleft()
                
                if isValid(curr):
                    level_results.add(curr)
                    found = True
                
                # If we haven't found a valid string yet, generate next states by removing one parenthesis
                if not found:
                    for i in range(len(curr)):
                        if curr[i] not in ('(', ')'):
                            continue
                        next_str = curr[:i] + curr[i + 1:]
                        if next_str not in visited:
                            visited.add(next_str)
                            queue.append(next_str)
                            
            if found:
                return list(level_results)
                
        return [""]
        