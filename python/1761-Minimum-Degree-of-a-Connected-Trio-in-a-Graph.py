# Time Complexity: O(n^3)
# Space Complexity: O(n^2)

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        degree = [0] * (n + 1)
        connected = [[False] * (n + 1) for _ in range(n + 1)]

        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            connected[u][v] = True
            connected[v][u] = True

        res = float("inf")

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if connected[i][j]:
                    for k in range(j + 1, n + 1):
                        if connected[i][k] and connected[j][k]:
                            res = min(res, degree[i] + degree[j] + degree[k] - 6)

        return -1 if res == float("inf") else res
