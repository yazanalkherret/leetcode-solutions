# Bottom-up Dynamic Programming
# Time Complexity: O(r*c)
# Space Complexity: O(r*c)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        # Edge case: Bottom-right corner is blocked
        dp[ROWS][COLS] = 0 if obstacleGrid[ROWS - 1][COLS - 1] else 1

        DIRS = [(-1, 0), (0, -1)]

        for r in range(ROWS, 0, -1):
            for c in range(COLS, 0, -1):

                for dr, dc in DIRS:
                    newR, newC = r + dr, c + dc
                    if obstacleGrid[newR - 1][newC - 1] == 1:
                        dp[newR][newC] = 0
                    else:
                        dp[newR][newC] += dp[r][c]

        return dp[1][1]

# Recursive DFS
# TLE

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        DIRS = [(1, 0), (0, 1)]

        def dfs(r, c):
            if obstacleGrid[r][c] == 1:
                return 0

            if (r, c) == (ROWS - 1, COLS - 1):
                return 1

            paths = 0
            for dr, dc in DIRS:
                newR, newC = r + dr, c + dc
                if newR < ROWS and newC < COLS:
                    paths += dfs(newR, newC)

            return paths

        
        return dfs(0, 0)
                