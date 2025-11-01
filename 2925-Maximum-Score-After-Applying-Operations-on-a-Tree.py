# Time Complexity: O(V+E)
# Space Complexity: O(V+E)

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        sumValues = sum(values)

        return sumValues - self.sumOfMins(adj, values, 0) 

    
    def sumOfMins(self, adj, values, node, parent = -1):
        if len(adj[node]) == 1 and adj[node][0] == parent:
            return values[node]
        
        sumOfChildMins = 0
        for nei in adj[node]:
            if nei == parent: continue

            sumOfChildMins += self.sumOfMins(adj, values, nei, node)

        return min(values[node], sumOfChildMins)