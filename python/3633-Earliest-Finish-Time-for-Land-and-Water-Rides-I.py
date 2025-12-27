# Bruteforce
# Time Complexity: O(m*n)
# Space Complexity: O(1)

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        res = float("inf")
        
        for i in range(n):
            startx, durationx = landStartTime[i], landDuration[i]
            endx = startx + durationx
            for j in range(m):
                starty, durationy = waterStartTime[j], waterDuration[j]
                waitTime = 0 if endx > starty else starty - endx

                res = min(res, endx + waitTime + durationy)

        for i in range(m):
            startx, durationx = waterStartTime[i], waterDuration[i]
            endx = startx + durationx
            for j in range(n):
                starty, durationy = landStartTime[j], landDuration[j]
                waitTime = 0 if endx > starty else starty - endx

                res = min(res, endx + waitTime + durationy)

        return res