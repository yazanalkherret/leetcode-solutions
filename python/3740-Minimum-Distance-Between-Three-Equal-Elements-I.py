# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)

        for i, num in enumerate(nums):
            indices[num].append(i)

        ans = float("inf")
        for num, vals in indices.items():
            if len(vals) >= 3:
                for i in range(2, len(vals)):
                    ans = min(ans,
                             abs(vals[i] - vals[i - 1]) +
                             abs(vals[i - 1] - vals[i - 2]) +
                             abs(vals[i] - vals[i - 2])
                             )


        return -1 if ans == float("inf") else ans
        