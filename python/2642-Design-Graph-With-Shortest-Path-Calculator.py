class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        #self.shortestPathCache = {}
        self.adj = defaultdict(list)
        self.size = n

        for src, dest, weight in edges:
            self.adj[src].append((weight, dest))        

    def addEdge(self, edge: List[int]) -> None:
        # Invalidate cache
        #self.shortestPathCache = {}

        src, dest, weight = edge
        self.adj[src].append((weight, dest))
        self.size += 1

    def shortestPath(self, node1: int, node2: int) -> int:
        #if (node1, node2) in self.shortestPathCache:
        #    return self.shortestPathCache[(node1, node2)]

        # Dijkstra's Algorithm
        distance = [float("inf")] * self.size
        seen = set()
        pq = [(0, node1)]

        while pq:
            weight, node = heapq.heappop(pq)

            if node in seen: continue

            seen.add(node)
            distance[node] = weight

            # Cache the shortest distance
            #self.shortestPathCache[(node1, node)] = weight

            if node == node2: break

            for neiWeight, nei in self.adj[node]:
                if nei not in seen:
                    heapq.heappush(pq, (weight + neiWeight, nei))

        return -1 if distance[node2] == float("inf") else distance[node2]
