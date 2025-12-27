class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            prev1, prev2 = 0, 0
            for num in nums:
                prev1, prev2 =  max(num + prev2, prev1), prev1
            return prev1

        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))