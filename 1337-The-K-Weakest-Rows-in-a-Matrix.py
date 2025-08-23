# Hashmap solution
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        soldiers = defaultdict(list)

        for r in range(ROWS):
            numSoldiers = 0
            for c in range(COLS):
                if mat[r][c]:
                    numSoldiers += 1
            soldiers[numSoldiers].append(r)

        res = []
        for key in sorted(soldiers.keys()):
            if len(res) >= k:
                return res[:k]
            for val in soldiers[key]:
                res.append(val)

        return res[:k]
            

# MinHeap Solution
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            strength = sum(row)
            heapq.heappush(heap, (strength, i))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res