# DP Solution is possible


# Naive Bruteforce
# Time Complexity: O(n^4)
# Space Complexity: O(n^2 + m^2)

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        subS, subT = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            for j in range(i, len(s)):
                subS[s[i:j + 1]] += 1

        for i in range(len(t)):
            for j in range(i, len(t)):
                subT[t[i:j + 1]] += 1
        
        count = 0
        seen = set()
        for substr in subS:
            if substr in seen: continue
            seen.add(substr)
            for i in range(len(substr)):
                for j in range(26):
                    currChar = chr(j + ord("a"))
                    if currChar == substr[i]: continue

                    temp = list(substr)
                    temp[i] = currChar
                    temp = "".join(temp)

                    if temp in subT:
                        count += (subT[temp] * subS[substr])
                
        return count
