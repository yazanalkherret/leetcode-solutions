class NumArray:

    def __init__(self, nums: List[int]):
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        self.preSum = []
        curr = 0
        for num in nums:
            curr += num
            self.preSum.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        # Time Complexity: O(1)

        if left == 0: return self.preSum[right]

        return self.preSum[right] - self.preSum[left - 1]