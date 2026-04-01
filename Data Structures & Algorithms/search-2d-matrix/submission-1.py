class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        # NOW FIND OUT IN WHICH ROW IS THE TARGET VALUE WOULD BE LOCATED
        top = 0
        bottom = rows - 1

        while top<=bottom:
            row = (top+bottom) // 2
        #WE ARE LOOKING AT THE LARGEST(RIGHTMOST) VALUE IN THE ROW
            if matrix[row][-1] < target: 
                top = row + 1
        # AGAIN BUT NOW WITH THE LEFTMOST VALUE
            elif matrix[row][0] > target:
                bottom  = row - 1
        # IF NOW WITH THE RIGHTMOST VALUE
            else:
                break
        
        if not (top<=bottom):
            return False
    
        row = (top + bottom) // 2
        l = 0
        r = cols - 1

        while l <= r:        
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False