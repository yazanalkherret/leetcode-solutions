# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd_index = -1
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2:
                odd_index = i
                break

        return num[:odd_index + 1]
