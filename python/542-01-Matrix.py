# Could be solved by modifying the input matrix in place, and the solution would be a bit shorter
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        output = [[0] * COLS for _ in range(ROWS)]

        def inBounds(r, c):
            return not (r < 0 or c < 0 or r >= ROWS or c >= COLS)

        def findDistances(queue):
            # BFS
            visited = set(queue)
            steps = 0
            while queue:
                currLevel = []
                for _ in range(len(queue)):
                    currLevel.append(queue.popleft())

                for r, c in currLevel:
                    if mat[r][c]:
                        output[r][c] = steps

                    for dr, dc in DIRECTIONS:
                        newR, newC = r + dr, c + dc
                        if inBounds(newR, newC) and (newR, newC) not in visited:
                            queue.append((newR, newC))
                            visited.add((newR, newC))
                steps += 1

        # Loop through all elements
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if not mat[r][c]:
                    queue.append((r, c))

        findDistances(queue)
        return output