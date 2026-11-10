class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        stack<int> myStack;

        for (int i = 0; i < temperatures.size(); i++){
            if (myStack.empty() or temperatures[i] < temperatures[myStack.top()]){
                myStack.push(i);
            }
            else {
                while (!myStack.empty() and temperatures[i] > temperatures[myStack.top()]){
                    int diff = i - myStack.top();
                    res[myStack.top()] = diff;
                    myStack.pop();
                }
            }
            myStack.push(i);

        }

        while (!myStack.empty()){
            myStack.pop();
        }
        return res;

        

    }


    
};
