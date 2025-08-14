class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l, r = 0, 2
        best = ""

        def isValid(arr):
            return arr[0] == arr[1] and arr[1] == arr[2]

        while r < len(num):
            curr = num[l:r+1]
            if isValid(curr):
                best = max(best, curr)
            l += 1
            r += 1
        return best