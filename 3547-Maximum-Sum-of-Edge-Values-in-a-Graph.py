# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        arrange = [0] * n

        l, r = 0, n - 1
        i = 1
        while l <= r:
            if l == r:
                arrange[l] = i
                break
            arrange[l] = i
            i += 1
            arrange[r] = i
            i += 1
            
            l += 1
            r -= 1

        for i in range(n - 1):
            arrange[i] = arrange[i] * arrange[i + 1]

        return sum(arrange) if len(edges) == n else sum(arrange[:-1])