# Time Complexity: O(n)
# Space Complexity: O(k)

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        longest = 0

        l = 0
        for r, c in enumerate(s):
            freq[c] += 1

            while len(freq) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            longest = max(longest, r - l + 1)

        return longest
