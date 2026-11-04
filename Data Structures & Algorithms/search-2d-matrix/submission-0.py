class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found = False
        for i in range(len(matrix)):
            j = 0
            k = len(matrix[i]) - 1
        

            while j <= k:
                mid = j + (k - j) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    j = mid + 1
                else:
                    k = mid - 1
        return found

            


