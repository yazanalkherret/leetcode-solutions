# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            
            if stack and stack[-1] == [char, k - 1]:
                stack.pop()
            elif stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])

        return "".join(char * freq for char, freq in stack)

