# Sorting
# Time Complexity: O(n logn) -> Sorting
# Space Complexity: O(n) -> Sorting/Output Array

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [ [x, i] for i, x in enumerate(score) ]
        score.sort(reverse= True)

        res = [None] * len(score)
        medals = { 0 : "Gold Medal", 1 : "Silver Medal", 2 : "Bronze Medal" }

        for i in range(len(score)):
            ndx = score[i][1]
            if i in (0, 1, 2):
                res[ndx] = medals[i]
            else:
                res[ndx] = str(i + 1)
        return res
    
# Heap
# Time Complexity: O(n logn)
# Space Complexity: O(n) or O(1) if res array isn't considered

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = [ (-x, i) for i, x in enumerate(score) ]
        heapq.heapify(score)

        res = [None] * len(score)
        medals = { 0 : "Gold Medal", 1 : "Silver Medal", 2 : "Bronze Medal" }

        for i in range(len(score)):
            _, ndx = heapq.heappop(score)
            if i in (0, 1, 2):
                res[ndx] = medals[i]
            else:
                res[ndx] = str(i + 1)
        return res