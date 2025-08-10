class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque()
        visited = set()

        def inBound(r, c):
            return r >= 0 and c >= 0 and r < ROWS and c < COLS

        # Find every border 'O'
        for c in range(COLS):
            if board[0][c] == 'O':
                queue.append((0, c))
            if board[ROWS-1][c] == 'O':
                queue.append((ROWS - 1, c))

        for r in range(ROWS):
            if board[r][0] == 'O':
                queue.append((r, 0))
            if board[r][COLS - 1] == 'O':
                queue.append((r, COLS - 1))

        # BFS
        while queue:
            r, c = queue.popleft()
            visited.add((r, c))

            for dr, dc in DIRECTIONS:
                new_r, new_c = r + dr, c + dc
                if(inBound(new_r, new_c) and
                    (new_r, new_c) not in visited and
                    board[new_r][new_c] == 'O'):
                    queue.append((new_r, new_c))

        # Modify the input in place
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'
        



