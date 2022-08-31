class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums[1:])
        nums.append(0)
        for i in range(1,len(nums)):
            if left == right:
                return i-1
            left = left+nums[i-1]
            right = right-nums[i]
        return -1
