class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        valid = set()

        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, values[i] ** -1))
            valid.add(a)
            valid.add(b)
        
        ans = []
        for a, b in queries:
            if a not in valid or b not in valid:
                ans.append(-1)
            else:
                ans.append(self.bfs(a, b, adj))

        return ans

    def bfs(self, src, dest, adj):
        seen = set()
        queue = deque([(src, 1)])

        while queue:
            curr, val = queue.popleft()
            if curr == dest:
                return val

            seen.add(curr)

            for nei, distance in adj[curr]:
                if nei not in seen:
                    queue.append((nei, distance * val))

        return -1
