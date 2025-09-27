# Time Complexity: O(n^3)
# Space Complexity: O(n^2)

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Adjacency Matrix
        distance = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            distance[i][i] = 0

        for src, dest, weight in edges:
            distance[src][dest] = weight
            distance[dest][src] = weight

        # Floyd-Warshall APSP
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], 
                                        distance[i][k] + distance[k][j])

        minheap = []
        for i in range(n):
            numCities = 0
            for j in range(n):
                if i == j: continue

                if distance[i][j] <= distanceThreshold:
                    numCities += 1

            heapq.heappush(minheap, (numCities, -i))

        return minheap[0][1] * -1


        