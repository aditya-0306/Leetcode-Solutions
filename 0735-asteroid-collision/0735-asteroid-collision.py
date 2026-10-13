

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            # Collision happens only when stack has a positive asteroid and current is negative
            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] < abs(ast):
                    stack.pop()
                    continue
                elif stack[-1] == abs(ast):
                    stack.pop()
                break
            else:
                stack.append(ast)
                
        return stack
        