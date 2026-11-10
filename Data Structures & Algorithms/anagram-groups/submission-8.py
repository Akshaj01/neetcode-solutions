class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create buckets
        buckets = defaultdict(list)
        res = []
        for string in strs:
            sortedstring = "".join(sorted(string))
            buckets[sortedstring].append(string)
        
        for r in list(buckets.values()):
            res.append(r)

        return res

        
        

        