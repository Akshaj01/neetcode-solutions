class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = {"}":"{", ")":"(", "]":"["}

        openStack = []

        for c in s:
            if c in closedToOpen: #closed
                if not openStack or openStack[-1] != closedToOpen[c]: #not right open or empty
                    return False
                openStack.pop()
            
            else: #open
                openStack.append(c)
        
        return not openStack
        