# Time Complexity: O(m + n)
# Space Complexity: O(m + n)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcdLength = gcd(len(str1), len(str2))
        ans = str1[:gcdLength]

        if (str1 == ans * (len(str1) // gcdLength) and
            str2 == ans * (len(str2) // gcdLength)):
            return "".join(ans)

        return ""

# Time Complexity: O(m + n)
# Space Complexity: O(m + n)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
