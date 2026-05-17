class Solution {
public:
int square(int n){
    int ans =0;
    while(n){
        int rem = n%10;
        n = n/10;
        ans+=pow(rem,2);
    }
    // cout<<ans<<" ";
    return ans;
    
}
    bool isHappy(int n) {
        vector<int> v(1000, 0); 
        while(n>=1){
                    if(n==1){
            return true;
        }
        cout<<v[n]<<" ";
        if(v[n] == square(n)){
            return false;
        }
        v[n]= square(n);
        n = square(n);

        }

        return true;


    }
};
