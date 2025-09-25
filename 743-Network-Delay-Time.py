# Dijkstra's Algorithm 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, dest, weight in times:
            adj[src].append([dest, weight])

        shortest = {}
        pq = [[0, k]]

        while pq:
            w1, n1 = heapq.heappop(pq)

            if n1 in shortest:
                continue

            shortest[n1] = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(pq, [w1 + w2, n2])

        for i in range(1, n + 1):
            if i not in shortest:
                return -1

        return max(shortest.values())