class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        ROWS, COLS = len(maze), len(maze[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inBounds(r, c):
            return r >= 0 and c >= 0 and r < ROWS and c < COLS

        def reachedEdge(r, c):
            return r == 0 or c == 0 or r == ROWS - 1 or c == COLS -1

        # Multisource BFS to find shortest path

        entrance = (entrance[0], entrance[1])
        queue = deque()
        visited = set()
        steps = 0
        queue.append(entrance)
        visited.add(entrance)

        while queue:
            currLevel = []
            for _ in range(len(queue)):
                currLevel.append(queue.popleft())

            for r, c in currLevel:
                if reachedEdge(r, c) and (r, c) != entrance:
                    return steps

                for dr, dc in DIRECTIONS:
                    newR, newC = r + dr, c + dc
                    if (inBounds(newR, newC) and
                        (newR, newC) not in visited and
                        maze[newR][newC] == '.'):

                        queue.append((newR, newC))
                        visited.add((newR, newC))

            steps += 1

        return -1