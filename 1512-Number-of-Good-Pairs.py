# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        seen = defaultdict(int)
        for num in nums:
            res += seen[num]
            seen[num] += 1

        return res