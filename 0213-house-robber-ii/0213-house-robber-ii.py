class Solution:
    def rob(self, nums: list[int]) -> int:
        # Base case: if there's only 1 house, rob it directly
        if len(nums) == 1:
            return nums[0]
            
        # Helper function from House Robber I (O(1) space)
        def house_robber_linear(sub_nums: list[int]) -> int:
            rob1, rob2 = 0, 0
            for num in sub_nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # Max between skipping the last house vs skipping the first house
        return max(
            house_robber_linear(nums[:-1]),  # Case 1: Excluding last house
            house_robber_linear(nums[1:])   # Case 2: Excluding first house
        )
        