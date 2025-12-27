# Time Complexity: O(m * unique(t))
# Space Complexity: O(m + n)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        relevant_chars = [char if char in freq_t else '*' for char in s]
        relevant_str = "".join(relevant_chars)

        m, n = len(s), len(t)
        freq_s, l = Counter(), 0
        minimum_window = float("inf")
        minimum_window_substr = ""
        for r, right_char in enumerate(relevant_str):
            freq_s[right_char] += 1
            if not self.isAccepted(freq_s, freq_t):
                continue
            
            while l < m and freq_s[relevant_str[l]] > freq_t[relevant_str[l]]:
                freq_s[relevant_str[l]] -= 1
                l += 1

            if (r - l + 1) < minimum_window:
                minimum_window = r - l + 1
                minimum_window_substr = s[l:r + 1]
        
        return minimum_window_substr



    def isAccepted(self, freq_s, freq_t):
        for key, val in freq_t.items():
            if val > freq_s[key]:
                return False
        return True
