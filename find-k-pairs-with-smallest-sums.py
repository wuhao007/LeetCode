import heapq
def kSmallestPairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
    stream = heapq.merge(*streams)
    print stream

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 10
print kSmallestPairs(nums1, nums2, k)
