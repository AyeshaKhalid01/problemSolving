class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            value=target-nums[i]
            if value in d:
                return [d[value], i]
            else:
                d[nums[i]]=i
