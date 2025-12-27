# This question can be solved more efficently with DP, Bitmasking
# Below is a backtracking solution

class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        visited = set()

        def backtrack(ndx):
            nonlocal res, visited
            if ndx == n + 1:
                res += 1
                return

            for j in range(1, n+1):
                if j in visited:
                    continue

                if j % ndx == 0 or ndx % j == 0:
                    visited.add(j)
                    backtrack(ndx + 1)
                    visited.remove(j)

        backtrack(1)
        return res