# Time Complexity: O(n)
# Space Complexity O(1)

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        max_fruits = 0
        freq = defaultdict(int)
        l = 0

        for r in range(n):
            freq[fruits[r]] += 1

            while len(freq) == 3:
                freq[fruits[l]] -= 1

                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]

                l += 1

            max_fruits = max(max_fruits, r - l + 1)

        return max_fruits
