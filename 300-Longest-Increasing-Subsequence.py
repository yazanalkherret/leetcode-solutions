# Patience Sort

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        patsort = []
        
        for i in nums:
            if not patsort or i > patsort[-1]:
                patsort.append(i)
            else:
                patsort[bisect.bisect_left(patsort, i)] = i
            
        return len(patsort)
