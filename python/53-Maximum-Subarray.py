# Rediscovered Kadane's Aglorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        before = float("-inf")
        maxx = float("-inf")

        for num in nums:
            before = max(0, num, num + before)
            if num < 0:
                maxx = max(maxx, num)
            else:
                maxx = max(maxx, before)

        return maxx