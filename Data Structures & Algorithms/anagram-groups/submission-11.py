from collections import defaultdict
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[list[str]]:
        buckets = defaultdict(list)
        #buckets
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            buckets[tuple(freq)].append(s)
        
        return list(buckets.values())




            
        
        




            

            

        




        

        

            


        