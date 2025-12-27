class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak, peakIndex = self.findPeak(mountainArr)
        if target > peak: return -1
        if target == peak: return peakIndex

        leftRes = self.bstLeft(mountainArr, target, 0, peakIndex - 1)
        if leftRes != -1: return leftRes

        rightRes = self.bstRight(mountainArr, target, peakIndex + 1, mountainArr.length() - 1)
        if rightRes != -1: return rightRes

        return -1


    def findPeak(self, arr) -> (int, int):
        # peak value, peak index
        l = 0
        r = arr.length() - 1

        while l <= r:
            m = (l + r) // 2
            prev, mid, nxt = arr.get(max(0, m - 1)), arr.get(m), arr.get(min(arr.length(), m + 1))
            if prev <= mid <= nxt:
                l = m + 1
            elif prev >= mid >= nxt:
                r = m - 1
            else:
                return mid, m


    def bstLeft(self, arr, target, start, end) -> int:
        minIndex = float("inf")
        while start <= end:
            m = (start + end) // 2
            mid = arr.get(m)
            if mid > target:
                end = m - 1
            elif mid < target:
                start = m + 1
            else:
                minIndex = min(minIndex, m)
                end = m - 1
                
        return minIndex if minIndex != float("inf") else -1

    def bstRight(self, arr, target, start, end) -> int:
        minIndex = float("inf")
        while start <= end:
            m = (start + end) // 2
            mid = arr.get(m)
            if mid < target:
                end = m - 1
            elif mid > target:
                start = m + 1
            else:
                minIndex = min(minIndex, m)
                end = m - 1
                
        return minIndex if minIndex != float("inf") else -1

        