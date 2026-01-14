# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        matrix = [[int(x) for x in row] for row in matrix]

        # Accumulation of heights
        for i in range(m - 2, -1, -1):
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i + 1][j]

        max_area = 0
        for i in range(m):
            prev_smaller, next_smaller = self.prev_next_smaller(matrix, i)
            
            for j in range(n):
                cur_area = (next_smaller[j] - prev_smaller[j] - 1) * matrix[i][j]
                max_area = max(max_area, cur_area)

        return max_area


    def prev_next_smaller(self, matrix, row):
        m, n = len(matrix), len(matrix[0])
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        
        stack = []
        for i in range(n):
            while stack and matrix[row][stack[-1]] > matrix[row][i]:
                pop_index = stack.pop()
                next_smaller[pop_index] = i

            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and matrix[row][stack[-1]] > matrix[row][i]:
                pop_index = stack.pop()
                prev_smaller[pop_index] = i

            stack.append(i)

        return prev_smaller, next_smaller
