class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = m*n - 1
        while low < high:
            mid = low + (high - low)//2
            print(mid, mid//n, mid%n, matrix[mid//n][mid%n])
            if matrix[mid//n][mid%n] >=target:
                high = mid
            else:
                low = mid + 1

        return matrix[low // n][low % n] == target

        