# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        depths = [0] * (n + 1)
        probs = [0] * (n + 1)
        hasChildren = [False] * (n + 1)
        adj = defaultdict(list)
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(parent, node, depth, prob):
            depths[node] = depth
            probs[node] = prob

            numChildren = len(adj[node]) - 1 if parent else len(adj[node])
            for child in adj[node]:
                if child == parent:
                    continue
                hasChildren[node] = True
                dfs(node, child, depth + 1, prob / numChildren)

        dfs(None, 1, 0, 1)
        if t == depths[target]:
            return probs[target]

        if t > depths[target] and not hasChildren[target]:
            return probs[target]

        return 0