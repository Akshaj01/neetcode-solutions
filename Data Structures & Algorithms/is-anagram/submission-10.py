from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_freq, t_freq = defaultdict(int), defaultdict(int)
        for char_s, char_t in zip(s, t):
            s_freq[char_s] += 1
            t_freq[char_t] += 1
        
        return s_freq == t_freq

            
            
        