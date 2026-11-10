class Solution:
    def isValid(self, s: str) -> bool:
        openStack = []
        closedToOpen = {"}" : "{", ")" : "(", "]" : "["}
        for c in s:
            #if closed:
            if c in closedToOpen:
                if not openStack or openStack[-1] != closedToOpen[c]:
                    return False
                openStack.pop()
            else:
                openStack.append(c)
        
        return not openStack