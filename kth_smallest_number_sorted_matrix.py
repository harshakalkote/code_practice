import heapq
def kth_smallest(k, mat):
    m = len(mat)
    n = len(mat[0])
    hp = []
    for i in xrange(n):
           heapq.heappush(hp,[mat[0][i], 0, i])
    heapq.heapify(hp)
    while k >1:
        x = heapq.heappop(hp)
        if x[1]+1 < m:
            heapq.heappush(hp,[mat[x[1]+1][x[2]], x[1]+1, x[2]])           
        heapq.heapify(hp)
        k-=1

    return hp[0][0]


print kth_smallest(8, [[1,10,12],[2,11,21], [3,31,45]])
