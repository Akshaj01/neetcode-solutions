class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (string i : strs){
            int len = i.length();
            res += to_string(len) + "#" + i;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        int j = 0;
        //first extract length
        while (i < s.size()){
            
            while (s[j] != '#'){
                j++;
            }

            int length = stoi(s.substr(i, j - i));
            i = j + 1;
            res.push_back(s.substr(i, length));
            i += length;
            j = i;
        }

        return res;
    }
};
