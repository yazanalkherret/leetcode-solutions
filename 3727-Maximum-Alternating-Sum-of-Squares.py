# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sortedSquared = sorted([num * num for num in nums])
        ans = 0
        mid = len(nums) // 2
        ans += sum(sortedSquared[mid:])
        ans -= sum(sortedSquared[:mid])
        return ans