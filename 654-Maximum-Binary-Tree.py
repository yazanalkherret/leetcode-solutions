# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        nodes = []
        for num in nums:
            node = TreeNode(num)
            while nodes and nodes[-1].val < num:
                node.left = nodes.pop()

            if nodes:
                nodes[-1].right = node

            nodes.append(node)

        return nodes[0]

# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return

        maxVal = nums[0]
        maxIndex = 0
        for i, num in enumerate(nums):
            if num > maxVal:
                maxVal = num
                maxIndex = i
        root = TreeNode(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex + 1:])

        return root