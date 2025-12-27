# Simplest Solution
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1

# Simulation
# Time Complexity: O(logn)
# Space Complexity: O(1)

class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches, winners = n // 2, ceil(n / 2)

        while winners != 1:
            matches += winners // 2
            winners = ceil(winners / 2)

        return matches
