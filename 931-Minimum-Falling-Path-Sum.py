# Top-down Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}
        DIRS = [(1, 0), (1, 1), (1, -1)]

        # Fill last row results
        for col in range(COLS):
            memo[(ROWS - 1, col)] = matrix[ROWS - 1][col]

        def fall(row, col):
            if (row, col) in memo:
                return memo[(row, col)]

            minSum = float("inf")
            for dr, dc in DIRS:
                newR, newC = row + dr, col + dc

                if (newR in range(0, ROWS) and
                    newC in range(0, COLS)):

                    minSum = min(minSum, matrix[row][col] + fall(newR, newC))

            memo[(row, col)] = minSum
            return minSum

        res = float("inf")
        for col in range(COLS):
            res = min(res, fall(0, col))
        print(memo)
        return res

# Bottom-up Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = [float("inf")] + matrix[ROWS - 1][::] + [float("inf")]

        for r in range(ROWS - 2, -1, -1):
            prev = memo[::]
            for c in range(COLS, 0, -1):
                minFall = min(prev[c - 1], prev[c], prev[c + 1])
                memo[c] = minFall + matrix[r][c - 1]

        return min(memo)