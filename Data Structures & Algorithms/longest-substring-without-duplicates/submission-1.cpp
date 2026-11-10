class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int r = 0;
        int cnt = 0;

        unordered_set<int> seen;

        while (r < s.size()){

            if (seen.count(s[r])){
                seen.erase(s[l]);
                l++;
                continue;
            }
            
            seen.insert(s[r]);
            int w = r - l + 1;
            cnt = max(cnt, w);
            r++;

        }
        return cnt;
    }
};
