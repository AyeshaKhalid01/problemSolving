class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        curr=""
        if len(s)%2 != 0:
            return False
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack.append(i)
            else:
                if stack==[]:
                    return False
                x=stack.pop()
                if (x=="(" and i!=")") or (x=="[" and i!="]") or (x=="{" and i!="}"):
                    return False
        if stack:
            return False
        return True
