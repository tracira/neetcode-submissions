class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s, dic_t = {}, {}
        for c in s:
            dic_s[c] = dic_s.get(c, 0) + 1
        for c in t:
            dic_t[c] = dic_t.get(c, 0) + 1
        
        return dic_s == dic_t