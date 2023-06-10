class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        while(left<=right):
            mid=(left+right)//2
            innerLeft=0
            innerRight=len(matrix[mid])-1
            if matrix[mid][innerLeft]<=target and matrix[mid][innerRight]>=target:
                while (innerLeft<=innerRight):
                    innerMid=(innerRight+innerLeft)//2
                    if matrix[mid][innerMid]<target:
                        innerLeft=innerMid+1
                    elif matrix[mid][innerMid]>target:
                        innerRight=innerMid-1
                    elif matrix[mid][innerMid]==target:
                        return True
                return False
            else:
                if matrix[mid][innerLeft]>target:
                    right=mid-1
                elif matrix[mid][innerRight]<target:
                    left=mid+1
        return False
