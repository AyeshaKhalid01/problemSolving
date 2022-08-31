class Solution:
    def reverseString(self, s: List[str]) -> None:
        high = len(s)-1
        self.helper(s, 0, high)
            
    def helper(self, s: List[str], low: int, hi: int) -> [str]:
        if (len(s) == 1) or (len(s) == 0) or low>=hi:
            pass
        else:
            temp = s[hi]
            s[hi] = s[low]
            s[low] = temp
            self.helper(s, low+1, hi-1)
