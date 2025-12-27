# Time Complexity: O(k logn + n)
# Space Complexity: O(n)

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        maxHeap = []
        # n
        for i in range(len(classes)):
            delta = (classes[i][0] + 1) / (classes[i][1] + 1) - (classes[i][0]/classes[i][1])
            maxHeap.append((-delta, i))

        heapq.heapify(maxHeap)
        # k * 2 * logn = k logn
        for _ in range(extraStudents):
            _, ndx = heapq.heappop(maxHeap)
            classes[ndx][0] += 1
            classes[ndx][1] += 1
            delta = (classes[ndx][0] + 1) / (classes[ndx][1] + 1) - (classes[ndx][0]/classes[ndx][1])
            heapq.heappush(maxHeap, (-delta, ndx))

        # n
        avg = sum([p/t for p, t in classes]) / len(classes)
        return avg