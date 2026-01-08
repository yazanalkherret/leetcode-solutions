# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def equalFrequency(self, word: str) -> bool:
        def equal_freq_helper():
            return len(set(v for v in freq.values() if v > 0)) == 1

        freq = Counter(word)
        for char in word:
            freq[char] -= 1
            if equal_freq_helper():
                return True
            freq[char] += 1

        return False