# Time Complexity: O(K) -> len(positions)
# Space Complexity: O(K)

class UnionFind:
    def __init__(self, positions):
        self.parent = [i for i in range(len(positions))]
        self.rank = [1 for _ in range(len(positions))]

    def find(self, v):
        res = self.parent[v]
        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]

        return res

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)

    def union(self, v1, v2):
        if self.connected(v1, v2): return False

        p1, p2 = self.find(v1), self.find(v2)

        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = self.parent[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = self.parent[p2]
            self.rank[p2] += self.rank[p1]

        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        union_find = UnionFind(positions)
        island_cells = {}
        num_islands = 0
        
        res = []
        for i, (row, col) in enumerate(positions):

            if (row, col) in island_cells:
                res.append(num_islands)
                continue

            for dr, dc in directions:
                nei_row, nei_col = row + dr, col + dc
                if ((nei_row, nei_col) in island_cells and
                    union_find.union(i, island_cells[(nei_row, nei_col)])):
                        num_islands -= 1

            num_islands += 1
            island_cells[(row, col)] = i
            res.append(num_islands)

        return res
