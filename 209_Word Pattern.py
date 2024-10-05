class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res={}
        s = s.split(" ")
        t = pattern
        if (len(s) != len(t)): return False
        for i in range(0,len(s)):
            if s[i] not in res:
                if t[i] in res.values():
                    return False
                res[s[i]]=t[i]
            if(res[s[i]]!=t[i]):
                return False
        return True
        
