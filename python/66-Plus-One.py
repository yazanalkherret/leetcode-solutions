# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0

        return [1] + digits

# Time Complexiy: O(n)
# Space Complextiy O(n)/O(1) -> result array

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        coef = 10 ** (len(digits) - 1)
        for d in digits:
            num += d * coef
            coef //= 10

        num += 1
        res = []
        while num != 0:
            res.append(num % 10)
            num //= 10
            
        res.reverse()
        return res if res else [0]