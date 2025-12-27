# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        n = len(capacity)
        prefix = capacity[::]
        valPrefixCount = defaultdict(int)
        valPrefixCount[(capacity[0], prefix[0])] = 1

        subarrays = 0
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

            leftVal = prefix[i - 1] - capacity[i]
            subarrays += valPrefixCount[(capacity[i], leftVal)]

            if capacity[i] == 0 and capacity[i - 1] == 0:
                subarrays -= 1

            valPrefixCount[(capacity[i], prefix[i])] += 1

        return subarrays