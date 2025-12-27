# Can be solved with BFS or DFS
# Below is a Recursive DFS Solution

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def isOutOfBounds(r, c):
            return r < 0 or c < 0 or r >= ROWS or c >= COLS

        def dfs(r, c):
            if isOutOfBounds(r, c):
                return 0
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0 # Mark visited
            localArea = 1

            for dr, dc in directions:
                localArea += dfs(r + dr, c + dc)
            return localArea



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(dfs(r, c), area)
        return area

