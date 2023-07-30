class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = self.helper(0, candidates, target, [], [])
        return result

    def helper(self, start, candidates, target, total, allTotals):
        if target==0:
            if total != None and allTotals != None:
                allTotals.append(total[:])
                return 
        if target <0:
            return
        for i in range(start, len(candidates)):
            total.append(candidates[i])
            self.helper(start, candidates, target-candidates[i], total, allTotals)
            total.pop()
            start+=1
        return allTotals

