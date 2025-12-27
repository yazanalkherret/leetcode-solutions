# DFS
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        copy = [row[::] for row in grid]

        def dfs(row, col):
            copy[row][col] = 0

            for dr, dc in directions:
                nei_row, nei_col = row + dr, col + dc
                if 0 <= nei_row < m and 0 <= nei_col < n and copy[nei_row][nei_col]:
                    dfs(nei_row, nei_col)

        for i in range(m):
            for j in range(n):
                if copy[i][j] and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    dfs(i, j)

        enclaves = 0
        for i in range(m):
            for j in range(n):
                if copy[i][j]:
                    enclaves += 1
        return enclaves

# Solution #2

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inBounds(r, c):
            return not (r < 0 or c < 0 or r == ROWS or c == COLS)

        def atEdge(r, c):
            return r == 0 or c == 0 or r == ROWS - 1 or c == COLS -1

        def dfs(r, c, size):
            nonlocal reachedEdge
            if atEdge(r, c):
                reachedEdge = True

            visited.add((r, c))
            size += 1
            for dr, dc in DIRECTIONS:
                newR, newC = r + dr, c + dc
                if (inBounds(newR, newC) and grid[newR][newC] and (newR, newC) not in visited):
                    size = max(dfs(newR, newC, size), size)
            return 0 if reachedEdge else size


        
        res = 0
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and (r, c) not in visited:
                    reachedEdge = False
                    res += dfs(r, c, 0)
        return res