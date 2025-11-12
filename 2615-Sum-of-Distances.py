class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        indices = defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)

        prefixes = defaultdict(list)

        for k, v in indices.items():
            prefixes[k] = v[::]
            for i in range(1, len(v)):
                prefixes[k][i] += prefixes[k][i - 1]

        ans = []

        for i, num in enumerate(nums):
            prefix = prefixes[num]
            ndx = bisect.bisect_left(indices[num], i)

            sumNext = prefix[-1] - prefix[ndx]
            sumPrev = prefix[ndx - 1] if ndx - 1 >= 0 else 0

            dnxt = sumNext - (len(prefix) - 1 - ndx) * i
            dprev = i * ndx - sumPrev

            ans.append(dnxt + dprev)

        return ans
