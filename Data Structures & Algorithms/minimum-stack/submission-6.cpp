class MinStack {
    private: 
        stack<int> minStack;
        stack<int> mainStack;

    public:

        void push(int val){
            if (minStack.empty()){
                minStack.push(val);
            }
            else {
                minStack.push(min(minStack.top(), val));
            }
            mainStack.push(val);
        } 

        void pop(void){
            mainStack.pop();
            minStack.pop();
        }

        int top(void){
            return mainStack.top();
        }
        
        int getMin(void){
            return minStack.top();
        }

};
