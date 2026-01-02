# DFS
# Time Complexity: O(V + E)
# Space Complexity: O(V)

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        def color_node(node, color):
            colors[node] = color

            for nei in graph[node]:
                if colors[nei] == -1:
                    if not color_node(nei, 0 if color else 1):
                        return False
                elif colors[nei] == colors[node]:
                    return False

            return True
                    

        for i in range(n):
            if colors[i] == -1:
                if not color_node(i, 0):
                    return False

        return True

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