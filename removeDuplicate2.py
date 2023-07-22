class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        unique=1
        for i in range(len(nums)-1):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
            if (nums[i]!=nums[i+1]) or d[nums[i]]<2:
                nums[unique]=nums[i+1]
                unique+=1
        return unique

