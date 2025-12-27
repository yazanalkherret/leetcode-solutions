# One-liner
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v > math.floor(len(nums) / 3) ]

# Can be solved with O(1) Space Complexity using Boyer-Moore Voting Algorithm