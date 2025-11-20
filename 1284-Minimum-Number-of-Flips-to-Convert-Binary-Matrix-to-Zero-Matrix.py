class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def inBound(row, col):
            return row >= 0 and row < m and col >= 0 and col < n

        def convertToTuple(state):
            return tuple(tuple(row) for row in state)

        def convertToList(state):
            return list(list(row) for row in state)

        seen = set()
        queue = deque([(convertToTuple(mat), 0)])
        goalState = convertToTuple([[0 for j in range(n)] for i in range(m)])

        while queue:
            currState, numTransitions = queue.popleft()
            if currState == goalState: return numTransitions
            if currState in seen: continue

            seen.add(currState)

            for i in range(m):
                for j in range(n):
                    reachableState = convertToList(currState)
                    
                    reachableState[i][j] = 0 if reachableState[i][j] else 1
                    
                    for dr, dc in DIRS:
                        newR, newC = i + dr, j + dc
                        if inBound(newR, newC):
                            reachableState[newR][newC] = 0 if reachableState[newR][newC] else 1

                    queue.append((convertToTuple(reachableState), numTransitions + 1))

        return -1
