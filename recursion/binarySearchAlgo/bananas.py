def canEat(piles: List[int], h: int, k: int) -> int:
    total=0
    if k==0:
        return False
    for i in piles:
        total+=-(-i//k)
    if total<=h:
        return True
    return False

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=0
        r=max(piles)
        prevTrue=None
        while(l<=r):
            m=(l+r)//2
            if canEat(piles, h, m) == True:
                if prevTrue==None:
                    prevTrue=m
                elif m<prevTrue:
                        prevTrue=m
                r=m-1
            else:
                l=m+1
        return prevTrue
