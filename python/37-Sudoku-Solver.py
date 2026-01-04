# Time Complexity: O((9!)^9) -> O(1)
# Space Complexity: O(81) -> O(1)

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        @lru_cache(None)
        def row_col_sub(cell_num):
            row, col = cell_num // 9, cell_num % 9
            sub = 3 * (row // 3) + col // 3
            return row, col, sub

        def is_valid(cell, num):
            row, col, sub = row_col_sub(cell)
            return (num not in seen_row[row]
                    and num not in seen_col[col]
                    and num not in seen_sub[sub])

        def backtrack(cell):
            if cell >= 81:
                return True

            row, col, sub = row_col_sub(cell)

            if board[row][col] != ".":
                return backtrack(cell + 1)

            for i in range(1, 10):
                if is_valid(cell, i):
                    board[row][col] = str(i)
                    seen_row[row].add(i)
                    seen_col[col].add(i)
                    seen_sub[sub].add(i)

                    if backtrack(cell + 1):
                        return True

                    seen_row[row].remove(i)
                    seen_col[col].remove(i)
                    seen_sub[sub].remove(i)
                    board[row][col] = "."

            return False

        seen_row, seen_col, seen_sub = defaultdict(set), defaultdict(set), defaultdict(set)

        for row in range(9):
            for col in range(9):
                sub = 3 * (row // 3) + col // 3
                if board[row][col] != ".":
                    val = int(board[row][col])
                    seen_row[row].add(val)
                    seen_col[col].add(val)
                    seen_sub[sub].add(val)

        backtrack(0)