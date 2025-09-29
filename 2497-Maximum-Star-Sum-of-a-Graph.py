class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        globalMax = max(vals) # Edge case of one node

        for src in adj:
            heap = []
            for nei in adj[src]:
                heapq.heappush(heap, -vals[nei])

            localMax = vals[src]
            i = 0
            while heap and i < k:
                localMax = max(localMax, localMax + (-heapq.heappop(heap)))
                i += 1

            globalMax = max(globalMax, localMax)

        return globalMax

# Simpler Solution

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(vals[b])
            adj[b].append(vals[a])

        globalMax = max(vals)  

        for src in range(len(vals)):
            neighbors = sorted(adj[src], reverse=True)

            localMax = vals[src]
            for i in range(min(k, len(neighbors))):
                if neighbors[i] <= 0:
                    break
                localMax += neighbors[i]

            globalMax = max(globalMax, localMax)

        return globalMax

           