# Simulation
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fivesTens = [0, 0]

        for bill in bills:
            if bill == 5:
                fivesTens[0] += 1
            elif bill == 10:
                if not fivesTens[0]:
                    return False
                fivesTens = [fivesTens[0] - 1, fivesTens[1] + 1]
            
            else:
                # 20
                if fivesTens[0] and fivesTens[1]:
                    fivesTens = [fivesTens[0] - 1, fivesTens[1] - 1]
                elif fivesTens[0] >= 3:
                    fivesTens = [fivesTens[0] - 3, fivesTens[1]]
                else:
                    return False
        return True