# Time Complexity: O(n log n) -> Timsort
# Space Complexity: O(n) -> events/Timsort

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        currNumOfPassengers = 0
        events = []
        
        for psngrs, frm, to in trips:
            events.append((frm, psngrs))
            events.append((to, -psngrs))

        events.sort()

        for _, psngrs in events:
            currNumOfPassengers += psngrs

            if currNumOfPassengers > capacity:
                return False

        return True