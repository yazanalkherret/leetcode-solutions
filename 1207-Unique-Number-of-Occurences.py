# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_elements = set(arr)
        unique_occurences = set(v for k, v in Counter(arr).items())

        return len(unique_elements) == len(unique_occurences)
