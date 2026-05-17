class Solution {
public:
    int calcOnes(int n){
        int q =0;
        int r =0;
        int res =0;
        while(n){
            q = n/2;
            r = n%2;
            n = q;
            res+=r;
            cout<<q<<" ";
        }
        return res;
    }
    vector<int> countBits(int n) {
        vector<int>v {0};
        
        for(int i =1; i<=n;i++){
            v.push_back(calcOnes(i));
        }
        return v;
    }
};
