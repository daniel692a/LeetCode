class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum, result;
        sum = 0;
        result = -10001;
        for(int i = 0; i < nums.size(); i++) {
            sum = max(sum+nums[i],nums[i]);
            if(sum > result) {
                result = sum;
            }
        }
        return result;
    }
};