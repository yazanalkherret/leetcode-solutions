# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0
        for i in range(n):
            even, odd = set(), set()
            for j in range(i, n):
                if not nums[j] & 1:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                if len(even) == len(odd):
                    longest = max(longest, j - i + 1)

        return longest