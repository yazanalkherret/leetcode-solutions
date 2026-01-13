# Time Complexity: O(n^2 log n)
# Space Complexity: O(n^2)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def in_bounds(row, col):
            return 0 <= row < n and 0 <= col < n

        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pq = [(grid[0][0], 0, 0)] # Elevation, Row, Col
        visited = set()

        # Pick smallest adjacent elevation
        while pq:
            elevation, row, col = heappop(pq)

            if (row, col) == (n - 1, n - 1):
                return elevation

            if (row, col) in visited: continue
            visited.add((row, col))

            for dr, dc in directions:
                next_r, next_c = row + dr, col + dc
                if in_bounds(next_r, next_c) and (next_r, next_c) not in visited:
                    heappush(pq, (max(elevation, grid[next_r][next_c]), next_r, next_c))


        return -1
