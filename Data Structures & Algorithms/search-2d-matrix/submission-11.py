class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l,r = 0, (rows * cols) -1

        while l <= r:
            mid = (l + r) // 2

            row = mid // cols
            col = mid % cols

            mid_value = matrix[row][col]

            if mid_value > target:
                r = mid - 1
                
            elif mid_value < target:
                l = mid + 1
            else:
                return True
        return False
        