# Non-optimal

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        minHeap = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                minHeap.append((arr[i]/arr[j], i, j))
        
        heapq.heapify(minHeap)

        for _ in range(k - 1):
            heapq.heappop(minHeap)

        _, i, j = heapq.heappop(minHeap)

        return [arr[i], arr[j]]
        