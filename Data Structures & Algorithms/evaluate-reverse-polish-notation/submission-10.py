class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+" , "-" , "*", "/"]
        myStack = []
        for i in tokens:
            if i in ops:
                b = int(myStack.pop())
                a = int(myStack.pop())
                if i == "/":
                    res = a / b
                elif i == "-":
                    res = a - b
                elif i == "*":
                    res = a * b
                else:
                    res = a + b
                myStack.append(res)

            else:
                myStack.append(i)
              
        return int(myStack[-1])