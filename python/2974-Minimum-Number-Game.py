# Sorting solution
# Time Complexity: O(n log n)
# Space Complexity: O(n) -> built-in sort, O(n) -> Output
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort() 
        arr = [] 

        for i in range(0, len(nums), 2):
            arr.append(nums[i + 1])
            arr.append(nums[i])
        return arr
    
# MinHeap solution
# Time Complexity: O(n log n)
# Space Complexity: O(n)
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums) 
        arr = []

        while nums:
            first, second = heapq.heappop(nums), heapq.heappop(nums)
            arr.append(second)
            arr.append(first)

        return arr