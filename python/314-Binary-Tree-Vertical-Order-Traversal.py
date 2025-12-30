# Time Complexity: O(NlogN)
# Space Complexity: O(N) -> Sorting

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        traversal = []
        queue = deque([(0, 0, 0, root)]) # col, row, left_order
    
        while queue:
            left_counter = 0
            for _ in range(len(queue)):
                col, row, index, cur = queue.popleft()
                traversal.append((col, row, index, cur.val))

                if cur.left:
                    queue.append((col - 1, row + 1, left_counter, cur.left))
                    left_counter += 1

                if cur.right:
                    queue.append((col + 1, row + 1, left_counter, cur.right))
                    left_counter += 1
        
        
        traversal.sort()
        max_col, min_col = traversal[-1][0], traversal[0][0]
        num_cols = max_col - min_col + 1

        res = [[] for _ in range(num_cols)]
        for col, _, _, val in traversal:
            res[col - min_col].append(val)

        return res
