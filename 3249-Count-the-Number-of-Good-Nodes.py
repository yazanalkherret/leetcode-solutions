# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        self.adj = defaultdict(list)

        for src, dest in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

        self.goodNodes = 0
        self.dfs(0, -1)
        return self.goodNodes 

    def dfs(self, curr, parent):
        totalInSubtree = 1

        childrenSizes = set()

        for child in self.adj[curr]:
            if child != parent:
                childSize = self.dfs(child, curr)
                totalInSubtree += childSize
                childrenSizes.add(childSize)

        if len(childrenSizes) in (0,1):
            self.goodNodes += 1

        return totalInSubtree