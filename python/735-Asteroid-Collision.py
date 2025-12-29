# Time Complexity: O(n)
# Space Complexity: O(1) -> Auxiliary

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:

            while stack and a < 0 and stack[-1] > 0 and stack[-1] < abs(a):
                stack.pop()
            
            if not stack or a > 0 or stack[-1] < 0:
                stack.append(a)
            elif stack[-1] == abs(a):
                stack.pop()

        return stack
