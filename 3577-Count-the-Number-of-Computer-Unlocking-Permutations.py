# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10 ** 9 + 7
        minn = complexity[0]
        res = 1
        for i in range(1, len(complexity)):
            num = complexity[i]
            
            if num < minn:
                return 0

            if num == complexity[0]:
                return 0

            res = (res * i) % MOD
        return res
