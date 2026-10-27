class Solution:
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = penalty = customers.count('Y')
        best_hour = 0
        
        for i, char in enumerate(customers):
            if char == 'Y':
                penalty -= 1
            else:
                penalty += 1
                
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1
                
        return best_hour
        