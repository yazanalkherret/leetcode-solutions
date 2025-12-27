# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)
        if n < k: return [] 
        original_freq = Counter(p)

        res = []
        l, r = 0, k - 1
        curr_freq = Counter(s[:k - 1])

        while r < n:
            curr_freq[s[r]] += 1
            if curr_freq == original_freq:
                res.append(l)

            curr_freq[s[l]] -= 1
            l += 1
            r += 1
        
        return res
