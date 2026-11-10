class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        for l in range(len(numbers)):
            diff = target - numbers[l]
            for r in range(l+1, len(numbers)):
                if (numbers[r] == diff): 
                    return [l+1,r+1]
            
        return -1
        