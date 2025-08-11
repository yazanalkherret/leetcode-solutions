class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        grid = isWater[::] # Copy


        def inBound(r, c):
            return r >= 0 and c >= 0 and r < ROWS and c < COLS

        queue = collections.deque()
        visited = set()

        # Flip values
        for r in range(ROWS):
            for c in range(COLS):
                # water cell
                if grid[r][c]:
                    grid[r][c] = 0
                    queue.append((r, c))
                    visited.add((r,c))

        while queue:
            currLevel = []
            for _ in range(len(queue)):
                currLevel.append(queue.popleft())

            for r, c in currLevel:
                for dr, dc in DIRECTIONS:
                    new_r, new_c = r + dr, c + dc
                    if inBound(new_r, new_c) and (new_r, new_c) not in visited:
                        grid[new_r][new_c] = grid[r][c] + 1
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))

        return grid