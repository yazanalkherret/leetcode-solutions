# Time Complexity: O(n^2 log n)
# Space Complexity: O(n^2)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Create adjacency list
        adj = defaultdict(list)
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            for j in range(i, n):
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                adj[i].append((distance, j))
                adj[j].append((distance, i))


        # Prim's Algorithm
        # Start from point 0    
        pq = [(0, 0)]
        visited = set([0])

        costMST = 0
        while len(visited) < n - 1:
            distance, dest = heapq.heappop(pq)
            
            if dest in visited:
                continue

            costMST += distance
            visited.add(dest)

            for adjacent in adj[dest]:
                if adjacent[1] not in visited:
                    heapq.heappush(pq, adjacent)

        return costMST

            