# Top-down Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        def helper(i):
            if i >= len(nums): return 0
            if memo[i] != -1: return memo[i]
            
            memo[i] = max(nums[i] + helper(i + 2), helper(i + 1))
            return memo[i]

        helper(0)
        return memo[0]

# Bottom-up Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = nums[::]
        memo.append(0)
        memo.append(0)

        for i in range(len(nums) - 1, -1, -1):
            memo[i] = max(memo[i] + memo[i + 2], memo[i + 1])
        return memo[0]

# Bottom-up Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for num in nums:
            prev1, prev2 =  max(num + prev2, prev1), prev1
        return prev1