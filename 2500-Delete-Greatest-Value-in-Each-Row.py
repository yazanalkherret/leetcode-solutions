# Time Complexity: O(m ∗ n logn)
# Space Complexity: O(1)

import heapq
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                grid[r][c] *= -1

        for row in grid:
            heapify(row)
        
        res = 0
        for c in range(COLS):
            maxx = 0
            for r in range(ROWS):
                maxx = max(heappop(grid[r]) * - 1, maxx)
            res += maxx

        return res

        