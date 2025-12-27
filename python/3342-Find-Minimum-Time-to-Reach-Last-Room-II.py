class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(moveTime), len(moveTime[0])
        # Dijkstra's Algorithm
        pq = [(0, 0, 0, 2)]
        visited = set()
        
        while pq:
            distance, i, j, lastStepCost = heapq.heappop(pq)

            if (i, j) in visited:
                continue

            currStepCost = 1 if lastStepCost == 2 else 2

            visited.add((i, j))
            if i == ROWS - 1 and j == COLS - 1:
                return distance

            for dr, dc in DIRECTIONS:
                newR, newC = i + dr, j + dc
                if self.inBounds(newR, newC, ROWS, COLS) and (newR, newC) not in visited:
                    delta = max(0, moveTime[newR][newC] - distance)
                    heapq.heappush(pq, (distance + delta + currStepCost, newR, newC, currStepCost))


    def inBounds(self, r, c, ROWS, COLS):
        return r >= 0 and r < ROWS and c >= 0 and c < COLS

        
