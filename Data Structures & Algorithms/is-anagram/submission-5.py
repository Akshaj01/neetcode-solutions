class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqmap_s = defaultdict(int)
        freqmap_t = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(0, len(s)):
            freqmap_s[s[i]] += 1
            freqmap_t[t[i]] += 1
        
        return freqmap_s == freqmap_t
            
            
        