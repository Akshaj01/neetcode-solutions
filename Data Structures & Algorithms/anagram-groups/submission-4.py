class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map_to_strings = {}

        for i in strs:
            freq = [0] * 26
            for c in i:
                freq[ord(c) - ord('a')] += 1
            if tuple(freq) not in map_to_strings:
                map_to_strings[tuple(freq)] = []

            map_to_strings[tuple(freq)].append(i)
        
        res = []
        
        for n in map_to_strings.values():
            res.append(n)
        
        return res

        




        

        

            


        