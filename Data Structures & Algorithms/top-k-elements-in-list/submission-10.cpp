class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count; //map for char to count
        unordered_map<int, vector<int>> frequencyMap; // frequency to numbers
        int mymax = 0;
        for (int i : nums){
            count[i]++;
            mymax = max(mymax, count[i]);
        }

        for (auto& pair : count){
            frequencyMap[pair.second].push_back(pair.first);
        }
        vector<int> res;
        
        for (int j = mymax ; j >= 0; j--){
                for (int number : frequencyMap[j]){
                    res.push_back(number);
                    if (res.size() == k){
                        return res;
                    }
                }
        }

        return {-1};
        
        
    }
};
