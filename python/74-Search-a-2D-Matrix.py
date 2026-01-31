# Time Complexity: O(log(m * n))
# Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_element = matrix[mid // n][mid % n]

            if mid_element < target:
                left = mid + 1

            elif mid_element > target:
                right = mid - 1

            else:
                return True

        return False

# Time Complexity: O(log(m * n))
# Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def bst_row(target):
            l, r = 0, m - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[mid][0] > target:
                    r = mid - 1
                elif matrix[mid][-1] < target:
                    l = mid + 1
                else:
                    return mid
            return 0

        def bst_col(row, target):
            l, r = 0, n - 1

            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] > target:
                    r = mid - 1
                elif matrix[row][mid] < target:
                    l = mid + 1
                else:
                    return True

            return False

        return bst_col(bst_row(target), target)
        