# Time Complexity: O(n logn)
# Space Complexity: O(n) for storing heap

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        minHeap = []

        for num in nums:
            if num:
                minHeap.append(num)
        
        heapq.heapify(minHeap)

        res = 0
        while minHeap:
            curr = heapq.heappop(minHeap)
            if curr <= 0:
                continue
            
            for i in range(len(minHeap)):
                minHeap[i] -= curr

            res += 1

        return res

# Clever solution using set
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            if num:
                unique.add(num)

        return len(unique)