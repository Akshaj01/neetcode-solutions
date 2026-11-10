class Solution {
public:
    int characterReplacement(string s, int k) {
        int max_w = 0;
        unordered_map<char, int> freq;
        int curr_w = 0;
        int l = 0;
        int max_f = 0;
        
        for (int r = 0; r < s.size(); r++){
            freq[s[r]]++;
            max_f = max(freq[s[r]], max_f);
            curr_w = r - l + 1;
            if (curr_w - max_f > k){
                freq[s[l]]--;
                l++;
                curr_w = 0;
                continue;
            }
            
            max_w = max(max_w, curr_w);
        }
        return max_w;
    }
};
