# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []
        for bracket in s:
            if bracket in hmap.values():
                stack.append(bracket)
            elif stack and stack[-1] == hmap[bracket]:
                stack.pop()
            else:
                return False
        return not stack

        # if bracket is opening
        # elif bracket is closing and matches the type at the top of the stack
        # else (bracket is closing and doesn't match)

        # return true if nothing left in the stack else false