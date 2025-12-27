# N^2 Solution with Hashmap
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        neighbors = defaultdict(list)
        res = 0

        for src, dest in roads:
            neighbors[src].append(dest)
            neighbors[dest].append(src)
            degrees[src] += 1
            degrees[dest] += 1

        for i in range(n - 1):
            for j in range(i + 1, n):
                curr = degrees[i] + degrees[j]
                if i in neighbors[j]: curr -= 1
                res = max(res, curr)

        return res

# N^2 Solution with hashset
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        road_set = set()
        for src, dest in roads:
            degree[src] += 1
            degree[dest] += 1
            road_set.add((src, dest))

        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = degree[i] + degree[j]
                if (i, j) in road_set or (j, i) in road_set:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank