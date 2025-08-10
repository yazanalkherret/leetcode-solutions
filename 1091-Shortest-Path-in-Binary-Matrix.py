class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        target = (N - 1, N - 1)
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

        def outBounds(r, c):
            return r < 0 or c < 0 or r >= N or c >= N

        queue = deque()
        visited = set()
        if not grid[0][0]:
            queue.append((0, 0))
            visited.add((0, 0))

        # BFS
        steps = 1
        while queue:
            current = []

            # Needed to count levels one by one
            for _ in range(len(queue)):
                current.append(queue.popleft())

            for r, c in current:
                if (r, c) == target and not grid[r][c]:
                    return steps

                for dr, dc in DIRECTIONS:
                    newR, newC = r + dr, c + dc

                    if (not outBounds(newR, newC) and
                    (newR, newC) not in visited and
                    not grid[newR][newC]):

                        queue.append((newR, newC))
                        visited.add((newR, newC))
            steps += 1

        return -1
