# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        conversion = {
            'I' : 1,
            'IV' : 4,
            'V' : 5,
            'IX' : 9,
            'X' : 10,
            'XL' : 40,
            'L' : 50,
            'XC' : 90,
            'C' : 100,
            'CD': 400,
            'D' : 500,
            'CM' : 900,
            'M' : 1000
        }


        ptr = 0
        res = 0
        while ptr < len(s):

            if ptr + 1 < len(s) and s[ptr : ptr + 2] in conversion:
                res += conversion[s[ptr : ptr + 2]]
                ptr += 2
            else:
                res += conversion[s[ptr]]
                ptr += 1

        return res
