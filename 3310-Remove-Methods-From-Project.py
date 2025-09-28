# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        suspicious = set()

        # Create Adjacency Map
        adj = defaultdict(list)
        for src, dest in invocations:
            adj[src].append(dest)    

        def dfs(node):
            if node in suspicious:
                return

            suspicious.add(node)
            for nei in adj[node]:
                dfs(nei)

        dfs(k)

        for src, dest in invocations:
            if src not in suspicious and dest in suspicious:
                return [i for i in range(n)]

        return [i for i in range(n) if i not in suspicious] 