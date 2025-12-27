# Time Complexity: O(n log(s/k))
# Space Complexity: O(1)

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def doable(x):
            curr_chunk = 0
            chunks = 0
            for piece in sweetness:
                curr_chunk += piece

                if curr_chunk >= x:
                    chunks += 1
                    curr_chunk = 0

                if chunks == k + 1:
                    return True

            return False

        lo, hi = 1, sum(sweetness) // (k + 1)
        res = 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if doable(mid):
                lo = mid + 1
                res = mid
            else:
                hi = mid - 1
        return res
