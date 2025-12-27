# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0    
        
        for i in range(N):
            # Odd palindromes
            l, r = i, i
            while l >= 0 and r < N and s[l] == s[r]:
                res += 1
                l, r = l - 1, r + 1

            # Even palindromes
            l, r = i, i + 1
            while l >= 0 and r < N and s[l] == s[r]:
                res += 1
                l, r = l - 1, r + 1

        return res