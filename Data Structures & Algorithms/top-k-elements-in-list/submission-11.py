class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = defaultdict(list)
        #freq counter
        freq = Counter(nums)
        #put nums into their count bucket
        for num, count in freq.items():
            buckets[count].append(num)
        #for n to 0 append to res until we hit k sized res
        for j in range(len(nums), 0, -1) :
            for num in buckets[j]:
                res.append(num)
                if (len(res) == k):
                    return res


       



            

        

        

        