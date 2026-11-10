class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) +  "#" + s
        return res

    def decode(self, strs: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(strs):
            while strs[j] != "#":
                j += 1
            length = int(strs[i:j])
            i = j + 1
            newString = strs[i: i + length]
            res.append(newString)
            i = i + length 
            j = i
            
        return res
        
