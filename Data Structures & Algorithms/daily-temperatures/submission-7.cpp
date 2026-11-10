class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int t_size = temperatures.size();
        vector<int> res(t_size, 0);
        stack<int> myStack;

        for (int i = 0; i < temperatures.size(); i++){
            if (myStack.empty()){
                myStack.push(i);
                continue;
            }

            while (!myStack.empty() and temperatures[myStack.top()] < temperatures[i]){
                res[myStack.top()] = i - myStack.top();
                myStack.pop();
            }

            myStack.push(i);
        }

        while (!myStack.empty()){
            res[myStack.top()] = 0;
            myStack.pop();
        }

        return res;

        

    }


    
};
