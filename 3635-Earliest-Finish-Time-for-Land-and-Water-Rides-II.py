# Time Complexity: O(m + n)
# Space Complexity: O(1)

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        minFinishLand, minFinishWater = float("inf"), float("inf")
        minFinishOverall = float("inf")
        for i in range(n):
            minFinishLand = min(minFinishLand, landStartTime[i] + landDuration[i])

        for j in range(m):
            minFinishWater = min(minFinishWater, waterStartTime[j] + waterDuration[j])
            # Check if you picked land first
            waitTime = max(0, waterStartTime[j] - minFinishLand)
            minFinishOverall = min(minFinishOverall, minFinishLand + waitTime + waterDuration[j])

        for i in range(n):
            # Check if you picked water first
            waitTime = max(0, landStartTime[i] - minFinishWater)
            minFinishOverall = min(minFinishOverall, minFinishWater + waitTime + landDuration[i])

        return minFinishOverall