# Time Complexity: O(klogk)
# Space Complexity: O(k)

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        pairs = []
        visited = set()
        minHeap = [(nums1[0] + nums2[0], 0, 0)]
        
        while minHeap and len(pairs) < k:
            summ, i, j = heapq.heappop(minHeap)
            if (i, j) in visited: continue

            visited.add((i, j))
            pairs.append([nums1[i], nums2[j]])

            if i + 1 < n:
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], i + 1, j))
            if j + 1 < m:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))

        return pairs
