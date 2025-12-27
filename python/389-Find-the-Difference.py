# Time Complexity: O(s + t)
# Space Complexity: O(26) -> O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        bucket = [[0, 0] for _ in range(26)] # (Freq T, Freq S)
        
        for char in t:
            bucket[ord(char) - ord('a')][0] += 1

        for char in s:
            bucket[ord(char) - ord('a')][1] += 1

        for i in range(26):
            freqT, freqS = bucket[i][0], bucket[i][1]
            if freqT != freqS:
                return chr(i + ord('a'))

# Interesting XOR solution
# Time Complexity: O(s + t)
# Space Complexity: O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        
        # XOR all characters in s and t
        for char in s + t:
            res ^= ord(char)
        
        # Convert the XOR result back to character
        return chr(res)