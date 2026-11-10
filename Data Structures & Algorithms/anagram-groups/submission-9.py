class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create buckets
        buckets = defaultdict(list)
        res = []
        for string in strs:
            sortedstring = "".join(sorted(string))
            buckets[sortedstring].append(string)

        return list(buckets.values())

        
        

        