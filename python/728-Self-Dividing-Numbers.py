# Time Complexity: O(n * d)
# Space Complexity: O(n)

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        self_dividing_nums = []

        for num in range(left, right + 1):
            if self.is_self_dividing(num):
                self_dividing_nums.append(num)

        return self_dividing_nums

    def is_self_dividing(self, num):
        if num == 0: return False
        
        num_copy = num

        while num_copy > 0:
            digit = num_copy % 10
            if digit == 0 or num % digit != 0:
                return False
            num_copy //= 10

        return True