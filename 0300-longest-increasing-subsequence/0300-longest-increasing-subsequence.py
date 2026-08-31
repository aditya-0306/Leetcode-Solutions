


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for num in nums:
            # Find the index of the first element >= num
            idx = bisect.bisect_left(tails, num)
            
            # If num is larger than all elements in tails, extend the subsequence
            if idx == len(tails):
                tails.append(num)
            else:
                # Otherwise, update the existing tail to keep potential subsequences as small as possible
                tails[idx] = num
                
        return len(tails)
        