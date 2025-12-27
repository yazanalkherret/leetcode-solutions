# Time Complexity: O(n logd)
# Space Complexity: O(n)

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:

        def can_achieve_tastiness(tastiness):
            last_price = price[0]
            count = 1

            for i in range(1, len(price)):
                if price[i] - last_price >= tastiness:
                    count += 1
                    last_price = price[i]

                if count == k:
                    return True

            return False

        price.sort()
        res = 0
        lo, hi = 0, ceil(price[-1] / (k - 1))
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_achieve_tastiness(mid):
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return res
