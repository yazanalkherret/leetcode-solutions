class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def inBounds(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def findIsland(r, c):
            # BFS
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                currLevel = []
                for _ in range(len(queue)):
                    currLevel.append(queue.popleft())

                for r, c in currLevel:
                    for dr, dc in DIRECTIONS:
                        newR, newC = r + dr, c + dc
                        if (inBounds(newR, newC) and
                            (newR, newC) not in visited and
                            grid[newR][newC]):
                            queue.append((newR, newC))
                            visited.add((newR, newC))

        def bridge():
            # BFS
            queue = deque(visited)
            steps = 0
            while queue:
                currLevel = []
                for _ in range(len(queue)):
                    currLevel.append(queue.popleft())

                for r, c in currLevel:
                    for dr, dc in DIRECTIONS:
                        newR, newC = r + dr, c + dc
                        if (inBounds(newR, newC) and
                            (newR, newC) not in visited):
                            
                            if grid[newR][newC]:
                                return steps
                            queue.append((newR, newC))
                            visited.add((newR, newC)) 
                steps += 1

        for r in range(ROWS):
            for c in range(COLS):
                if not visited and grid[r][c] == 1:
                    findIsland(r, c)

        return bridge()

# Can be more concise if DFS is used instead of BFS in findIsland(r, c)