class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int min_price = prices[0];
        for (auto &price:prices)
        {
            int profit = price - min_price;
            max_profit = max(profit,max_profit);
            min_price = min(price,min_price);
        }
        return max_profit;
    }
};