class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["+", "-", "*", "/"]
        valStack = []
        for token in tokens:
            if token in operations:
                b = int(valStack.pop())
                a = int(valStack.pop())
                if token == "+":
                    val = a + b
                    valStack.append(val)
                if token == "-":
                    val = a - b
                    valStack.append(val)
                if token == "*":
                    val = a * b
                    valStack.append(val)
                if token == "/":
                    val = int(a / b)
                    valStack.append(val)
            else:
                valStack.append(int(token))
        return valStack[-1]
                    



        
                


        