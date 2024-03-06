class Solution(object):
    def searchMatrix(self, matrix, target):
        rows,columns = len(matrix),len(matrix[0])
        top,bottom=0,rows-1
        while top<=bottom:
            row = (top+bottom)//2
            if matrix[row][0]>target:
                bottom = row -1
            elif matrix[row][-1]<target:
                top = row+1
            else:
                break
        left,right=0,columns-1
        while left<=right:
            mid = (left+right)//2
            if matrix[row][mid]>target:
                right = mid-1
            elif matrix[row][mid]<target:
                left = mid+1
            else:
                return True
        return False
