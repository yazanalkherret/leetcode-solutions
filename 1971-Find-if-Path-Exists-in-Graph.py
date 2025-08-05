class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)
        for v1, v2 in edges:
            neighbors[v1].append(v2)
            neighbors[v2].append(v1)

        def dfs(curr, target, visited):
            if curr == target:
                return True
            if curr in visited:
                return False

            visited.add(curr)
            res = False
            for neighbor in neighbors[curr]:
                res = res or dfs(neighbor, target, visited)

            return res

        return dfs(source, destination, set())