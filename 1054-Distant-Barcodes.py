# Time Complexity: O(nlogk) -> k : Unique Elements
# Space Complexity: O(n)

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = Counter(barcodes)
        ans = []

        heap = [ (-f, barcode) for barcode, f in freq.items() ]
        heapq.heapify(heap)
        temp = None
        while heap or temp:
            if temp:
                heapq.heappush(heap, temp)
                temp = None

            negFreq, barcode = heapq.heappop(heap)

            if ans and ans[-1] == barcode:
                temp = (negFreq, barcode)
                negFreq, barcode = heapq.heappop(heap)

            ans.append(barcode)
            if negFreq + 1 < 0:
                heapq.heappush(heap, (negFreq + 1, barcode))

        return ans