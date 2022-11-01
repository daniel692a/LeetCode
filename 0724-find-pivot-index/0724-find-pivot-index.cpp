class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        vector<int> prefix(nums.size()+1);
        int sum=0;
        prefix[0] = sum;
        for(int i=0; i<nums.size(); i++){
            sum+=nums[i];
            prefix[i+1]=sum;
        }
        for(int i=1; i<prefix.size(); i++){
            if(prefix[i-1]==(prefix[prefix.size()-1]-prefix[i])){
                return i-1;
            }
        }
        return -1;
    }
};