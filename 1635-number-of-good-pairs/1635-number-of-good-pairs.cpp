class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int, int> cnt;
        int pairs = 0;
        for(int i=0; i<nums.size(); i++){
            if(cnt[nums[i]]){
                cnt[nums[i]] = (cnt[nums[i]]) + 1;
            } else {
                cnt[nums[i]] = 1;
            }
        }
        for(auto elem : cnt){
            pairs += (elem.second*(elem.second-1))/2;
        }
        return pairs;
    }
};