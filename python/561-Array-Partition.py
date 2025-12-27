# Time Complexity: O(nlogn)
# Space Complexity: O(n) -> Sorting

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        maxSum = 0
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            maxSum += nums[i]
        return maxSum
