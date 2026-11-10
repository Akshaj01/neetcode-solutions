class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0;
        int maxSize = 0;
        unordered_map<char, int> freq;
        int maxFreq = 0;

        for (int r = 0; r < s.size(); r++){
            freq[s[r]]++;
            maxFreq = max(maxFreq, freq[s[r]]);
            int windowSize = r - l + 1;
            while (windowSize - maxFreq > k){
                freq[s[l]]--;
                l++;
                windowSize = r - l + 1;
            }
            maxSize = max(maxSize, windowSize);
        }
        return maxSize;
    }
};
