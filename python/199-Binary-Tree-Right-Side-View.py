# BFS
# Time Complexity: O(n)
# Space Complexity: O(d)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        res = []
        queue = deque([root])

        while queue:
            cur_level = []
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                cur_level.append(cur_node.val)

                if cur_node.left:
                    queue.append(cur_node.left)
                
                if cur_node.right:
                    queue.append(cur_node.right)

            res.append(cur_level[-1])

        return res
        