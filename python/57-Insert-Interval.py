# Time Complexity: O(n)
# Space Complexity: O(1) Auxiliary

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, new_interval)
        p_start, p_end = intervals[0]
        res = []

        for start, end in intervals[1:]:
            if start <= p_end:
                p_end = max(p_end, end)
            else:
                res.append([p_start, p_end])
                p_start, p_end = start, end

        res.append(([p_start, p_end]))
        return res
