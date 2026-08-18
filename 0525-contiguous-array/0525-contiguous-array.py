class Solution:
    def findMaxLength(self, nums):
        first = {0: -1}
        balance = 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 0:
                balance -= 1
            else:
                balance += 1

            if balance in first:
                max_len = max(max_len, i - first[balance])
            else:
                first[balance] = i

        return max_len