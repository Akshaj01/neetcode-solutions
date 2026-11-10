class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        buckets = defaultdict(list)
        for num, count in freq.items():
            buckets[count].append(num)
        
        res = []
        i = len(nums)
        while i > 0:
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
            i -= 1



            

        

        

        