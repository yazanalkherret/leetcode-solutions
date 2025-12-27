class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        GA, GB, UNVISITED = 1, -1, 0
        group = [UNVISITED] * len(graph)

        def bfs(i):
            if group[i]:
                return True

            queue = deque([i])
            group[i] = GA

            while queue:
                curr = queue.popleft()
                for nei in graph[curr]:
                    if group[curr] == group[nei]:
                        return False
                    elif not group[nei]:
                        queue.append(nei)
                        group[nei] = -1 * group[curr]
            return True


        for i in range(len(graph)):
            if not bfs(i):
                return False

        return True