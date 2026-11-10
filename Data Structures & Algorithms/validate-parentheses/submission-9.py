class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {"}" : "{", "]" : "[", ")" : "(" }
        openStack = []
        for i in s:
            if i in closedToOpen: # closed
                if openStack and openStack[-1] == closedToOpen[i]:
                    openStack.pop()
                    continue
                else:
                    return False

            else: #open
                openStack.append(i)  
        
        return not openStack