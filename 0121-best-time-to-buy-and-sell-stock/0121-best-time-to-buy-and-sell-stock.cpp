class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_historical=INT_MAX;
        int max_profit=0;
        for(int i=0; i<prices.size(); i++){
            min_historical = min(min_historical, prices[i]);
            max_profit = max(max_profit, prices[i]-min_historical);
        }
        return max_profit;
    }
};