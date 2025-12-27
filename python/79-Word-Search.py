class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) - 1
        n = len(board[0]) - 1

        visited = set()

        def cell_index(row, col):
            return row * (n + 1) + col
            

        def out_of_bounds(row, col):
            return row > m or col > n or row < 0 or col < 0

        def find_word(row, col, str_ndx):
            if cell_index(row, col) in visited:
                return False

            if out_of_bounds(row, col):
                return False

            cell = board[row][col]
            if cell != word[str_ndx]:
                return False

            if str_ndx == len(word) - 1:
                return True

            visited.add(cell_index(row, col))
            # Adjacents
            res = (
                    find_word(row + 1, col, str_ndx + 1) or
                    find_word(row - 1, col, str_ndx + 1) or
                    find_word(row, col + 1, str_ndx + 1) or
                    find_word(row, col - 1, str_ndx + 1)
                    )

            

            visited.remove(cell_index(row, col))

            return res

        res = False
        for i in range(m + 1):
            for j in range(n + 1):
                res = res or find_word(i, j, 0)
                visited.clear()

        return res