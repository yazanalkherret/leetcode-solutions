# Time Complexity: O(nlogn) -> Timsort
# Space Complexity: O(n) -> Timsort

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        h = sorted(horizontalCut)
        v = sorted(verticalCut)
        
        sumV = sum(v)
        sumH = sum(h)

        sumAns = 0
        while h and v:
            if h[-1] > v[-1]:
                sumAns += h[-1] + sumV
                sumH -= h[-1]
                h.pop()
            else:
                sumAns += v[-1] + sumH
                sumV -= v[-1]
                v.pop()

        return sumAns + sumV + sumH