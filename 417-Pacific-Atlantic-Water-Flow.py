class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(heights), len(heights[0])
        pacific = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        atlantic = [[0 for _ in range(COLS)] for _ in range(ROWS)] 
        res = []

        def dfs(r, c):
            if(r < 0 or c < 0 or r == ROWS or c == COLS or pacific[r][c] == 1):
                return

            pacific[r][c] = 1

            for dr, dc in DIRECTIONS:
                new_r, new_c = r + dr, c + dc
                if new_r < ROWS and  new_c < COLS and heights[new_r][new_c] >= heights[r][c]:
                    dfs(new_r, new_c)

        def dfsAtlantic(r, c):
            if(r < 0 or c < 0 or r == ROWS or c == COLS or atlantic[r][c] == 1):
                return

            atlantic[r][c] = 1

            if pacific[r][c] == 1:
                res.append([r, c])

            for dr, dc in DIRECTIONS:
                new_r, new_c = r + dr, c + dc
                if new_r < ROWS and  new_c < COLS and heights[new_r][new_c] >= heights[r][c]:
                    dfsAtlantic(new_r, new_c)        


        # start pacific
        for r in range(ROWS):
            for c in range(COLS):
                dfs(0, c)
                dfs (r, 0)

        # start Atlantic
        for r in range(ROWS):
            for c in range(COLS):
                dfsAtlantic(ROWS - 1, c)
                dfsAtlantic(r, COLS - 1)                
        return res