

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_count, closed_count, current_string):
            if len(current_string) == 2 * n:
                res.append(current_string)
                return
                
            if open_count < n:
                backtrack(open_count + 1, closed_count, current_string + "(")
                
            if closed_count < open_count:
                backtrack(open_count, closed_count + 1, current_string + ")")
                
        backtrack(0, 0, "")
        return res
        