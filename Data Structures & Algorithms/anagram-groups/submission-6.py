class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create buckets
        buckets = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            buckets[tuple(count)].append(string)
        
        return list(buckets.values())
        