# Time Complexity: O(n)
# Space Complexity: Result Array -> O(n), Extra Space -> O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        for i in range(n - 1):
            prefix[i + 1] = prefix[i] * nums[i]

        currSuffix = 1
        for i in range(n - 1, -1, -1):
            prefix[i] = currSuffix * prefix[i]
            currSuffix *= nums[i]

        return prefix