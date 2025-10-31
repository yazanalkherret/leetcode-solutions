// Time Complexity: O(n)
// Space Complexity: O(1)
// TLE in Python

class Solution {
public:
    long long minEnd(int n, int x) {
        long long lastNum = x;
        for (int i = 0; i < n - 1; i++) {
            lastNum = (lastNum + 1) | x;
        }
        return lastNum;
    }
};
