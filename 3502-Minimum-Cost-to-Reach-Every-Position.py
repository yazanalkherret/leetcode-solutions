# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        runningMin = float("inf")
        ans = []
        for c in cost:
            runningMin = min(runningMin, c)
            ans.append(runningMin)

        return ans
        