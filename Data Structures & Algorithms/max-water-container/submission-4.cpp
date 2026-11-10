class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1;
        int maxArea = 0;
        while (l < r){
            int height = min(heights[l] , heights[r]);
            int width = r - l;
            int area = height * width;
            maxArea = max(maxArea, area);
            if (heights[r] <= heights[l]){
                r--;
            }
            else{
                l++;
            }
        }
        return maxArea;

    }
};
