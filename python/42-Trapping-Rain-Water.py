# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left, right = 0, n - 1
        left_max = height[0]
        right_max = height[-1]
        res = 0
        
        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [height[0]] * n
        right_max = [height[-1]] * n

        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        res = 0

        for i in range(1, n - 1):
            min_bounds = min(left_max[i], right_max[i])
            res += min_bounds - height[i]

        return res
        