class Solution {
public:
    int square(int n) {
        int ans = 0;
        while (n) {
            int rem = n % 10;
            n = n / 10;
            ans += pow(rem, 2);
        }
        return ans;
    }

    bool isHappy(int n) {
        unordered_set<int> visited;
        while (n != 1) {
            if (visited.count(n) > 0) {
                return false;
            }
            visited.insert(n);
            n = square(n);
        }
        return true;
    }
};