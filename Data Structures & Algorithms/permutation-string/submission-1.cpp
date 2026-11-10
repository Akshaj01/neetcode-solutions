class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int l = 0;
        vector<int> freq_s1(26,0);
        vector<int> freq_s2(26,0);

        if (s1.size() > s2.size()) return false;
        for (int i = 0; i < s1.size(); i++){
            freq_s1[s1[i]- 'a']++;
            freq_s2[s2[i]- 'a']++;
        }

        if (freq_s1 == freq_s2) return true;

        for (int r = s1.size(); r < s2.size(); r++){
            freq_s2[s2[l]- 'a']--;
            freq_s2[s2[r]- 'a']++;

            if (freq_s2 == freq_s1) return true;

            l++;
        }

        return false;

        
    }
};
