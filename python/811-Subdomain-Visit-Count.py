# Time Complexity: O(n*m)
# Space Complexity: O(n*m)

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq_split = [cpdomain.split(" ") for cpdomain in cpdomains]
        freq_subdomains = [[int(temp[0]), temp[1].split(".")] for temp in freq_split]

        count = defaultdict(int)
        for freq, subdomains in freq_subdomains:
            for i in range(len(subdomains)):
                count[".".join(subdomains[i:])] += freq

        return [str(c) + " " + subd for subd, c in count.items()]
