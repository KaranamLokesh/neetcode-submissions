class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        total = m*n
        low, high = 0, total-1
        while low<high:    
            mid = low + (high-low+1)//2
            if matrix[mid//n][mid%n] > target:
                high = mid-1
            else:
                low = mid
        return matrix[low//n][low%n] == target
        
        