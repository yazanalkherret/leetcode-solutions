# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        numOfMostFreq = 0
        maxx = max(freq.values())
        for val in freq.values():
            if val == maxx:
                numOfMostFreq += 1

        return numOfMostFreq * maxx