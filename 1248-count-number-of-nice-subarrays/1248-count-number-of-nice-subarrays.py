
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k):
            res = 0
            left = 0
            odds = 0
            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    odds += 1
                while odds > k:
                    if nums[left] % 2 != 0:
                        odds -= 1
                    left += 1
                res += right - left + 1
            return res

        return at_most(k) - at_most(k - 1)
        