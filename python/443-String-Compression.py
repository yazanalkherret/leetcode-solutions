# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        r_ptr, w_ptr = 0, 0
        cur_repeat = 0

        for r_ptr, cur_char in enumerate(chars):
            cur_repeat += 1

            if r_ptr == n - 1 or cur_char != chars[r_ptr + 1]:
                chars[w_ptr] = cur_char
                w_ptr += 1

                if cur_repeat != 1:
                    for digit in str(cur_repeat):
                        chars[w_ptr] = digit
                        w_ptr += 1

                cur_repeat = 0

        for _ in range(n - w_ptr):
            chars.pop()

        return len(chars)
