class Solution {
public:
    int reverse(int x) {
        int res = 0;
        const int MIN = -2147483648; // -2^31
        const int MAX = 2147483647;  // 2^31 - 1
        while(x){
            int rem = x%10;
            x = x/10;
                        if (res > MAX / 10 || (res == MAX / 10 && rem > MAX % 10))
                return 0;
            if (res < MIN / 10 || (res == MIN / 10 && rem < MIN % 10))
                return 0;
            res = res*10 + rem;
        }
        return res;
        
    }
};
