# Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(V, pV):
            subtree[V] = values[V]

            for v in adj[V]:
                if v == pV: continue

                dfs(v, V)
                subtree[V] += subtree[v]
                dp[V] += dp[v]
                    
            
            if subtree[V] % k == 0:
                dp[V] += 1

        
        subtree = [0] * n # Subtree values
        dp = [0] * n
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dfs(0, None)
        return dp[0]