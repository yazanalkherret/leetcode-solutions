# Bruteforce solution
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixandSuffix(str1, str2):
            print(str1, str2)
            isPrefix = str2[:len(str1)] == str1

            suffixStart = len(str2) - len(str1)
            isSuffix = str2[suffixStart:] == str1
            
            return isSuffix and isPrefix

        
        n = len(words)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if isPrefixandSuffix(words[i], words[j]):
                    res += 1

        return res