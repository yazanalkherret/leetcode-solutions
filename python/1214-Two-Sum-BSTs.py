# Time Complexity: O(NlogM)
# Space Complexity: O(Hn + Hm)

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def helper(root1, root2, target):
            if not root1:
                return False

            if self.find(root2, target - root1.val):
                return True

            return helper(root1.left, root2, target) or helper(root1.right, root2, target)

        return helper(root1, root2, target)
            

    def find(self, root, target):
        if not root:
            return False

        if root.val == target:
            return True
        elif root.val > target:
            return self.find(root.left, target)
        else:
            return self.find(root.right, target)
