class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # BFS Level Order Traversal
        # With node indices for each level
        
        # Level indices represent the left to right order of a level if it was complete (no null nodes)

        queue = deque([(root, 0)]) # Node, Its index in its level
        max_width = 1 # Final result

        while queue:

            # Level variables
            level_length = len(queue)
            left_most_index = queue[0][1]
            right_most_index = queue[-1][1]

            max_width = max(max_width, right_most_index - left_most_index + 1)

            for _ in range(level_length):
                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left, index * 2))

                if node.right:
                    queue.append((node.right, index * 2 + 1))

        return max_width

        # N: Number of nodes in the tree
        # Time Complexity: O(N)

        # Space Complexity: O(D), Diameter of a tree (Widest level) 
        # Worst-case: O(N/2) -> O(N)
