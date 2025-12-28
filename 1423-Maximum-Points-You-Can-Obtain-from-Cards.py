# Sliding Window
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n: return sum(cardPoints)
        prefix_sum = [cardPoints[0]]

        for i in range(1, n):
            prefix_sum.append(prefix_sum[-1] + cardPoints[i])

        total_sum = prefix_sum[-1]

        window_size = n - k
        l = 0
        max_points = 0
        
        for r in range(window_size - 1, n):
            right_sum, left_sum = prefix_sum[r], prefix_sum[l - 1] if l - 1 >= 0 else 0
            window_sum = right_sum - left_sum
            curr_points = total_sum - window_sum
            max_points = max(max_points, curr_points)
            l += 1

        return max_points
