class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int answer = 0;
        int i=0;
        while(i<nums.size()){
            if(nums[i]==1){
                int count = 1;
                i++;
                while(i<nums.size() and nums[i]==1){
                    count++;
                    i++;
                }
                answer = max(answer, count);
            } else {
                i++;
            }
        }
        return answer;
    }
};