class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = set()

        def dfs(curr, visited):
            visited.add(curr)

            for i in range(n):
                if i not in visited and isConnected[curr][i] != 0:
                    dfs(i, visited)

        for i in range(n):
            if i not in visited:
                dfs(i, visited)
                provinces += 1

        return provinces