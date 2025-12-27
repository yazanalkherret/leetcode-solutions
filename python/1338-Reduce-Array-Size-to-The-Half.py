# Time Complexity: O(n logn) -> while loop and heappop
# Space Complexity: O(n) -> counter and heap

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        maxHeap = [ -f for f in freq.values() ]
        heapq.heapify(maxHeap)

        currLen, res = len(arr), 0
        while currLen > len(arr) // 2:
            f = heapq.heappop(maxHeap)
            res += 1
            currLen += f # f is negative

        return res
