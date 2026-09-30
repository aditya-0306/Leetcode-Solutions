class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_res = 0
        curr_num = 0
        sign = 1
        
        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char in "+-":
                curr_res += sign * curr_num
                curr_num = 0
                sign = 1 if char == '+' else -1
            elif char == '(':
                # Push current result and sign onto stack
                stack.append(curr_res)
                stack.append(sign)
                curr_res = 0
                sign = 1
            elif char == ')':
                curr_res += sign * curr_num
                curr_num = 0
                # Multiply by sign before parenthesis, then add previous result
                curr_res *= stack.pop()
                curr_res += stack.pop()
                
        curr_res += sign * curr_num
        return curr_res
        