class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = l + 1;
        int maxP = 0;

        while (r < prices.size()){
            int profit = 0;
            if (prices[r] > prices[l]){
                profit = prices[r] - prices[l];
            }
            else {
                l = r;
                r = l + 1;
                continue;
            }

            maxP = max(maxP, profit);
            r++;
        }

        return maxP;
    }
};
