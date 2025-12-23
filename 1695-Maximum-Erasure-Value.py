# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix_sum = [0]
        for i, num in enumerate(nums):
            prefix_sum.append(prefix_sum[-1] + num)

        last_seen = {}
        max_sum = 0
        l = 0
        for r, num in enumerate(nums):
            if num in last_seen and last_seen[num] >= l:
                l = last_seen[num] + 1
            last_seen[num] = r

            max_sum = max(max_sum, prefix_sum[r + 1] - prefix_sum[l])

        return max_sum
