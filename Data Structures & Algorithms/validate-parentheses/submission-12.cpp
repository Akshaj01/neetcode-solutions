class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> closedToOpen = { {')' , '('}, {'}' , '{'}, {']' , '['} };
        stack<char> openStack;

        for (char c: s){
            //if closed
            if (closedToOpen.count(c)){
                if (openStack.empty() || openStack.top() != closedToOpen[c]){
                    return false;
                }
                openStack.pop();
            }
            //if open 
            else {
                openStack.push(c);
            }
        }

        return openStack.empty();
    }
};
