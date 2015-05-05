f = open("B-small-attempt0.in", "r")
T = int(f.readline())


import heapq
def barber(B, N, M):
    pq = []
    for i in range(B):
        N -= 1
        if N == 0:
            return i + 1
        else:
            heapq.heappush(pq, (M[i], i))
    for _ in range(N - 1):
        t, n = heapq.heappop(pq)
        heapq.heappush(pq, (t + M[n], n))
    return heapq.heappop(pq)[1] + 1

    
for t in range(T):
    B, N = map(lambda x : int(x), f.readline().split())
    M = map(lambda x : int(x), f.readline().split())
    print "Case #" + str(t + 1) + ": " + str(barber(B, N, M))
f.close()
