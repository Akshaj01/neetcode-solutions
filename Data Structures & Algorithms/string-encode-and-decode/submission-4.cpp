class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        for (const string& s: strs){
            res += to_string(s.length()) + "#" + s;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        while (i < s.length()){
            //find the #
            int j = i;
            while (s[j] != '#'){
                j++;
            }
            // get length
            int len = stoi(s.substr(i, j - i));

            //move i to start of string
            i = j + 1;

            // push string to result vector
            res.push_back(s.substr(i, len)); 

            //move i to next chain
            i += len;
        }


        return res;

        
    }
};
