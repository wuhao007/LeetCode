class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        
        def searchRange(A, target, head, tail):
            
            def find_head(A, head, tail):
                if A[head] == A[tail]:
                    return head
                else:
                    mid = (head + tail)/2
                    if A[mid] < A[tail]:
                        return find_head(A, mid+1, tail)
                    elif A[mid] == A[tail]:
                        return find_head(A, head+1, mid)
                        
            def find_tail(A, head, tail):
                if A[head] == A[tail]:
                    return tail
                else:
                    mid = (head + tail)/2
                    if A[head] < A[mid]:
                        return find_tail(A, head, mid-1)
                    elif A[head] == A[mid]:
                        return find_tail(A, mid, tail-1)                    
                    
                
            if head > tail:
                return [-1, -1]
            else:
                mid = (head + tail)/2
                if target > A[mid]:
                    return searchRange(A, target, mid + 1, tail)
                elif target < A[mid]:
                    return searchRange(A, target, head, mid - 1)
                else:
                    return [find_head(A, head, mid), find_tail(A, mid, tail)]
        if target < A[0] or target > A[-1]:
            return [-1, -1]
        return searchRange(A, target, 0, len(A) - 1)
            
solution = Solution()
print solution.searchRange([1,2,3,3,3,3,4,5,9],3)
