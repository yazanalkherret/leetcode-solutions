# Time Complexity: O(nlogn)
# Space Complexity: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        num_rooms = 0
        heap = []
        intervals.sort()

        for start, end in intervals:
            while heap and heap[0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, end)
            num_rooms = max(num_rooms, len(heap))
            
        return num_rooms
