class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        bucket = [[] for _ in range(len(nums) + 1)]
        freq_of_num = {}
        for i in nums:
            freq_of_num[i] = freq_of_num.get(i, 0) + 1

        for i, f in freq_of_num.items():
            bucket[f].append(i)

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
        

        

        
        