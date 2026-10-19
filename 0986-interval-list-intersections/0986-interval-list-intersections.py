

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        
        while i < len(firstList) and j < len(secondList):
            start_max = max(firstList[i][0], secondList[j][0])
            end_min = min(firstList[i][1], secondList[j][1])
            
            # Check if there is an intersection
            if start_max <= end_min:
                res.append([start_max, end_min])
                
            # Advance the pointer of the interval that ends first
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                
        return res
        