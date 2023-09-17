class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome=""
        length=0
        for i in range(len(s)):
            l,r=i,i
            palindrome,length=self.helper(s,l,r,palindrome, length)
            l,r=i,i+1
            palindrome,length=self.helper(s,l,r,palindrome, length)
        return palindrome


    def helper(self, s, l, r, res, resLen):
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1 > resLen):
                resLen=r-l+1
                res=s[l:r+1]
            l-=1
            r+=1
        return res, resLen
