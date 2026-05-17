class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int,int>mp;
        for(int i=0; i<nums.size(); i++){
            mp[nums[i]]++;
        }
        for(map<int,int>::iterator it = mp.begin(); it!=mp.end(); it++ ){
            if(it->second>1){
                return true;
            }
        }
        return false;
    }
};
