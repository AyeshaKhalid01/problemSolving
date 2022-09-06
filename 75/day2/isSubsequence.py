class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        if len(s)==0:
            return True
        pos=0
        for i in t:
            if i==s[pos]:
                pos+=1
            if len(s)==pos:
                return True
        return False
