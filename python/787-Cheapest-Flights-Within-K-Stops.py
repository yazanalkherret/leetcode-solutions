# Bellman-Ford
# Time Complexity: O(K(N + E))
# Space Complexity: O(N)

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [float("inf")] * n
        dist[src] = 0

        for i in range(k + 1):
            temp = dist[::]

            for start, end, price in flights:
                temp[end] = min(temp[end], dist[start] + price)

            dist = temp

        return dist[dst] if dist[dst] != float("inf") else -1
