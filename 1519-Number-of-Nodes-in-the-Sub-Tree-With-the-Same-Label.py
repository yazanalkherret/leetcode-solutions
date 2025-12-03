# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)


        res = [0] * n
        def dfs(curr, parent, freq):
            if adj[curr] == [parent]:
                freq[labels[curr]] += 1
                res[curr] = 1
                return freq

            for child in adj[curr]:
                if child == parent: continue

                for alpha, f in dfs(child, curr, defaultdict(int)).items():
                    freq[alpha] += f

            freq[labels[curr]] += 1
            res[curr] = freq[labels[curr]]
            return freq

        dfs(0, None, defaultdict(int))
        return res
