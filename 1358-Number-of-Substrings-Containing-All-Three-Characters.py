# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        substrs = 0
        l = 0
        freq = [0, 0, 0]  # a, b, c
        
        for r in range(n):
            freq[ord(s[r]) - ord('a')] += 1
            
            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                substrs += n - r
                freq[ord(s[l]) - ord('a')] -= 1
                l += 1
                
        return substrs
