# Top-down Dynamic Programming
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        res = 0
        def helper(row, col):
            nonlocal res
            if row >= ROWS or col >= COLS:
                return 0

            if (row, col) in cache:
                return cache[(row, col)]

            right = helper(row, col + 1)
            bottom = helper(row + 1, col)
            diag = helper(row + 1, col + 1)

            if matrix[row][col] == '0':
                cache[(row, col)] = 0
            else:
                cache[(row, col)] = 1 + min(right, bottom, diag)

            res = max(res, cache[(row, col)])
            return cache[(row, col)]

        helper(0, 0)
        return res ** 2

# Bottom-up Dynamic Programming
# Time Complexity: O(m*n)
# Space Complexity: O(1) -> Modified input

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        matrix.append([0] * COLS)
        matrix = [row + [0] for row in matrix]
        res = 0

        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                right = matrix[i][j + 1]
                bottom = matrix[i + 1][j]
                diag = matrix[i + 1][j+ 1]

                if matrix[i][j] == '1':
                    matrix[i][j] = 1 + min(right, bottom, diag)
                else: 
                    matrix[i][j] = 0

                res = max(res, matrix[i][j])

        return res ** 2