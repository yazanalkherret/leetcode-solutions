# Dijkstra's Algorithm 
# Time Complexity: O(m log n)
# Space Complexity: O(m + n)

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        n = len(disappear)
        ans = [-1] * n
        adj = [[] for _ in range(n)]

        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))

        pq = [(0, 0)]
        seen = set()
        while pq:
            currTime, node = heappop(pq)
            if node in seen: continue

            seen.add(node)
            ans[node] = currTime

            for nei, t in adj[node]:
                if nei in seen or currTime + t >= disappear[nei]:
                    continue

                heappush(pq, (currTime + t, nei))

        return ans
