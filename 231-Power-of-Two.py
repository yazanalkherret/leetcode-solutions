# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False 
        
        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2
        return True