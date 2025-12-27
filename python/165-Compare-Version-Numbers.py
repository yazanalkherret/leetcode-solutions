# Time Complexity: O(m + n), m -> len(version1), n -> len(version2)
# Space Complexity: O(1)

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1, l2, r1, r2 = [0] * 4

        while l1 < len(version1) or l2 < len(version2):
            r1, r2 = l1, l2
            # Version 1
            while r1 < len(version1) and version1[r1] != ".":
                r1 += 1

            part1 = int(version1[l1:r1]) if l1 < len(version1) else 0

            # Version 2
            while r2 < len(version2) and version2[r2] != ".":
                r2 += 1

            part2 = int(version2[l2:r2]) if l2 < len(version2) else 0

            # Comparison:
            if part1 > part2:
                return 1
            
            if part2 > part1:
                return -1

            l1 = r1 + 1
            l2 = r2 + 1

        return 0