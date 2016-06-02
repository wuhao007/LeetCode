class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l + 1 != r:
            mid = l + (r - l) / 2
            if matrix[midi/n][mid%n] == target:
                return True
            elif target < matrix[mid]:
                r = mid
            else:
                l = mid
        if mid[l/n][l%n] == target:
            return True
        elif mid[r/n][r%n] == target:
            return True
        else:
            return False
