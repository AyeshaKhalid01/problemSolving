class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb=[]
        curCombs=[]
        self.combinations(1,curCombs,comb, n, k)
        return comb
    
    def combinations(self, i, curCombs,comb, n, k):
        if len(curCombs)==k:
            comb.append(curCombs.copy())
        if i>n:
            return
        for j in range(i,n+1):
            curCombs.append(j)
            self.combinations(j+1,curCombs,comb, n, k)
            curCombs.pop()
