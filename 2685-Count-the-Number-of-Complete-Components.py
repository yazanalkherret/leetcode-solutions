# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        completeComponents = 0

        adj = defaultdict(list)

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        def dfs(src, components):
            components.append(src)
            visited.add(src)
            for nei in adj[src]:
                if nei not in visited:
                    dfs(nei, components)

            return components

        for i in range(n):
            if i in visited:
                continue

            components = dfs(i, [])
            numEdges = 0

            for vertix in components:
                numEdges += len(adj[vertix])

            if numEdges == len(components) * (len(components) - 1):
                completeComponents += 1

        return completeComponents 