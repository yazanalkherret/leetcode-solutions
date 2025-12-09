# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'e', 'u', 'A', 'E', 'I', 'O', 'E', 'U'])
        original_order = []

        for c in s:
            if c in vowels:
                original_order.append(c)

        res = []
        for c in s:
            if c in vowels:
                res.append(original_order.pop())
            else:
                res.append(c)

        return "".join(res)
