# MaxHeap Solution
# Time Complexity: O(n + n logn) -> O(n logn)
# Space Complexity: O(n)

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [ [-count, letter] for letter, count in count.items() ]
        heapq.heapify(maxHeap)

        res = []
        while maxHeap:
            count, letter = heapq.heappop(maxHeap)
            for _ in range(-count):
                res.append(letter)

        return "".join(res)