

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total_sum = sum(nums)
        
        def get_subset_sums(arr):
            res = [[] for _ in range(len(arr) + 1)]
            for i in range(1 << len(arr)):
                s = 0
                cnt = 0
                for j in range(len(arr)):
                    if (i >> j) & 1:
                        s += arr[j]
                        cnt += 1
                res[cnt].append(s)
            for k in range(len(res)):
                res[k].sort()
            return res
            
        left_sums = get_subset_sums(nums[:n])
        right_sums = get_subset_sums(nums[n:])
        
        ans = float('inf')
        target = total_sum // 2
        
        for k in range(n + 1):
            l_list = left_sums[k]
            r_list = right_sums[n - k]
            
            for l_val in l_list:
                rem = target - l_val
                idx = bisect.bisect_left(r_list, rem)
                
                if idx < len(r_list):
                    s1 = l_val + r_list[idx]
                    ans = min(ans, abs(total_sum - 2 * s1))
                if idx > 0:
                    s1 = l_val + r_list[idx - 1]
                    ans = min(ans, abs(total_sum - 2 * s1))
                    
        return ans
        