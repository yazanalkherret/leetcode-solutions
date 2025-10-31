class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # Arrival Time of the first sent packet =  distance * 2
        # Departure Time of the last sent packet = floor(firstArrives - 1 / patience) * patience
        # Ariival Time of the last sent packet = LastPacketSentTime + distance * 2

        n = len(patience)
        
        # BFS
        distance = [float("inf")] * n
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque([(0, 0)]) # Distance, Node
        seen = set()
        while q:
            d, node = q.popleft()
            if node in seen: continue

            distance[node] = d
            seen.add(node)

            for nei in adj[node]:
                if nei in seen: continue
                
                q.append((d + 1, nei))

        idleTime = float("-inf")

        for i in range(1, n):
            firstPacketArrivalTime = distance[i] * 2
            lastPacketSentTime = floor((firstPacketArrivalTime - 1) / patience[i]) * patience[i]
            lastPacketSentArrivalTime = lastPacketSentTime + distance[i] * 2
            
            idleTime = max(idleTime, lastPacketSentArrivalTime)

        return idleTime + 1