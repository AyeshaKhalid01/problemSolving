def subseq(string, left, lis=None):
   if lis==None:
      lis=[]
   if len(string)==0:
      if len(left)!=0:
         lis.append(left)
      return
   subseq(string[1:], left+string[0], lis)
   subseq(string[1:], left, lis)
   return lis


print(subseq("abc",""))
subseq("abc","")
