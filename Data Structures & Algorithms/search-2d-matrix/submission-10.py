class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_size = len(matrix)
        cols_size = len(matrix[0])

        #find the row
        l = 0
        r = rows_size - 1
        target_row = 0
        while l <= r:
            mid_row = (l + r) // 2
            if matrix[mid_row][0] <= target and target <= matrix[mid_row][-1]:
                target_row = mid_row
                break
            elif matrix[mid_row][-1] <= target:
                l = mid_row + 1
            else:
                r = mid_row - 1

        #find the item
        l = 0
        r = cols_size - 1
        while l <= r:
            mid_col = (l + r) // 2
            if matrix[target_row][mid_col] == target:
                return True
            elif matrix[target_row][mid_col] < target:
                l = mid_col + 1
            else:
                r = mid_col - 1
        
        return False




        