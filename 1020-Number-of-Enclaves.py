# Solution #1
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