# Dijkstra's Algorithm

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inBound(r, c):
            return r >= 0 and r < m and c >= 0 and c < n

        pq = [(0, (0, 0))]
        seen = set()
        while pq:
            currTime, curr = heappop(pq)
            if curr in seen: continue
            
            if curr == (m - 1, n -1):
                return currTime

            seen.add(curr)

            for dr, dc in DIR:
                newR, newC = curr[0] + dr, curr[1] + dc
                if not inBound(newR, newC): continue

                if (newR, newC) not in seen:
                    heappush(pq, ( currTime + max(0, moveTime[newR][newC] - currTime) + 1, (newR, newC) ))

        return -1