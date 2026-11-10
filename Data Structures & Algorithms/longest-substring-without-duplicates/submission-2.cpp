class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int maxLen = 0;
        unordered_map<char, int> freq;
        for (int r = 0; r < s.size(); r++){
            freq[s[r]]++;
            while (freq[s[r]] > 1){
                freq[s[l]]--;
                l++;
            }
            maxLen = max(maxLen, r - l + 1);

        }
        return maxLen;
    }
};
