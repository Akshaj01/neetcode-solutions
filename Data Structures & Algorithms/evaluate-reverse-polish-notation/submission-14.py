class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']
        valStack = []
        for c in tokens:
            if c in operations: #operation
                b = int(valStack.pop())
                a = int(valStack.pop())
                match c:
                    case '+':
                        newValue = a + b
                        valStack.append(newValue)
                    case '-':
                        newValue = a - b
                        valStack.append(newValue)
                    case '*':
                        newValue = a * b
                        valStack.append(newValue)
                    case '/':
                        newValue = int(a / b)
                        valStack.append(newValue)
            else: #number
                valStack.append(int(c))

        return valStack[-1]
                


        