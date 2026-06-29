class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n  = len(matrix), len(matrix[0])
        l, r = 0, m *n - 1

        while l <= r:
            mid = (r + l) // 2
            
            row = mid // n
            col = mid % n

            guess = matrix[row][col]

            if guess == target:
                return True

            if guess > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False