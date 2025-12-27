# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.globalMax = 0
        adj = defaultdict(list)

        for i, p in enumerate(parent):
            if i == 0: continue
            adj[p].append(i)

        def helper(parentNode, curr):
            longestChain, secondLongestChain = 0, 0
            for child in adj[curr]:
                longestChainStartingFromChild = helper(curr, child)

                if s[curr] == s[child]:
                    continue

                if longestChainStartingFromChild > longestChain:
                    secondLongestChain = longestChain
                    longestChain = longestChainStartingFromChild
                elif longestChainStartingFromChild > secondLongestChain:
                    secondLongestChain = longestChainStartingFromChild

            self.globalMax = max(self.globalMax, longestChain + secondLongestChain + 1)

            return 1 + longestChain

        helper(None, 0)
        return self.globalMax