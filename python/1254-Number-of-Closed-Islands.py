class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inBounds(r, c):
            return r >= 0 and r < ROWS and c >= 0 and c < COLS

        def dfs(r, c):
            visited.add((r, c))
            if r == 0 or c == 0 or r == ROWS -1 or c == COLS - 1:
                closed = False
            else:
                closed = True

            for dr, dc in DIRECTIONS:
                newR, newC = r + dr, c + dc
                if inBounds(newR, newC) and (newR, newC) not in visited and not grid[newR][newC]:
                    closed = dfs(newR, newC) and closed

            return closed
        
        res = 0
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if not grid[r][c] and (r, c) not in visited:
                    if dfs(r, c):
                        res +=1

        return res