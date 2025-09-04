# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        distance_xz = abs(x - z)
        distance_yz = abs(y - z)

        if distance_xz == distance_yz: return 0
        if distance_xz < distance_yz: return 1
        if distance_yz < distance_xz: return 2