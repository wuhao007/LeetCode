class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if n == 1:
            return 1

        count = 1
        start = 0
        end = A[0]
        new_end = end
        step = 0
        while end < n - 1:
            step = start
            new_end = end
            while start <= step <= end:
                if step + A[step] > new_end >= end:
                     new_end = step + A[step]
                     if new_end >= n - 1:
                         return count + 1
                step += 1
            if new_end <= end:
                return 
            else:
                start = end + 1
                end = new_end
                count += 1
        return count
solution = Solution()
print solution.jump([3,4,3,1,0,7,0,3,0,2,0,3])
#print solution.jump([1,1,1,1,1,1,1,1])
