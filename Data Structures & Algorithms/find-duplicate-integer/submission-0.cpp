class Solution {
public:
    
    int findDuplicate(vector<int>& nums) {
        unordered_set<int> mySet;
        for (int i : nums ){
            if (mySet.count(i)) return i;
            mySet.insert(i);
        }
        return -1;
    }
};
