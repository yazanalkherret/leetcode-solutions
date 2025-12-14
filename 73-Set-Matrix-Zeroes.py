# Time Complexity: O(n*m)
# Space Complexity: O(n+m)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeroed_rows, zeroed_cols = set(), set()
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    zeroed_rows.add(i)
                    zeroed_cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in zeroed_rows or j in zeroed_cols:
                    matrix[i][j] = 0
