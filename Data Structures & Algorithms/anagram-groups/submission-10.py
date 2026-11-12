from collections import defaultdict
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[list[str]]:
        buckets = defaultdict(list)
        #buckets
        for s in strs:
            freq = frozenset(Counter(s).items())
            buckets[freq].append(s)
        
        return list(buckets.values())




            
        
        




            

            

        




        

        

            


        