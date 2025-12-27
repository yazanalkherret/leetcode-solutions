class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                row, col = q.popleft() # Change to pop() to change the solution to iterative DFS
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if(new_row < 0 or new_col < 0 or
                        new_row >= ROWS or new_col >= COLS or
                        grid[new_row][new_col] == '0'):
                        continue
                    
                    q.append((new_row, new_col))
                    grid[new_row][new_col] = '0'

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1

        return islands

# Recursive DFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Out of bounds base case
            if(r < 0 or c < 0 or
                r >= ROWS or c >= COLS):
                return

            if grid[r][c] == '0':
                return

            grid[r][c] = '0'

            for dr, dc in directions:
                dfs(r + dr, c + dc)



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands