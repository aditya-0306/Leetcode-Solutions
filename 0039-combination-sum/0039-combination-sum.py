from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, current_path, current_sum):
            if current_sum == target:
                res.append(list(current_path))
                return
            if current_sum > target or i == len(candidates):
                return
            
            # Include the current candidate
            current_path.append(candidates[i])
            backtrack(i, current_path, current_sum + candidates[i])
            current_path.pop()
            
            # Exclude the current candidate and move to the next
            backtrack(i + 1, current_path, current_sum)
            
        backtrack(0, [], 0)
        return res
        