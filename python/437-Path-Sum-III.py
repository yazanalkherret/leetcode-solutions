# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        def helper(node, prev_sum, prefixes):
            nonlocal count
            if not node: return

            cur_sum = prev_sum + node.val
            count += prefixes[cur_sum - target_sum]

            prefixes[cur_sum] += 1

            helper(node.left, cur_sum, prefixes)
            helper(node.right, cur_sum, prefixes)
            prefixes[cur_sum] -= 1
        
        count = 0
        helper(root, 0, Counter({0 : 1}))
        return count
