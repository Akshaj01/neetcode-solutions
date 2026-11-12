class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [] # final result
        freq = defaultdict(int) # freqMap
        count = 0 # count in res
        
        #make freq map
        for i in nums:
            freq[i] += 1

        #put freq into buckets dictionary
        buckets = defaultdict(list)
        for c in freq:
            buckets[freq[c]].append(c)

        for i in range(len(nums), 0, -1):
            for v in buckets[i]:
                res.append(v)
                count += 1
                if count == k:
                    return res





        

        
        

        

        
        