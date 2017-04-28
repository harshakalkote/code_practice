def knapsack(W, weight, cost):
    #import pdb; pdb.set_trace()
    table = [0] * (W+1)
    for w in xrange(W+1):
        max_so_far = 0
        for i, wt in enumerate(weight):
            if wt <= w:
                cur = cost[i] + table[w-weight[i]]
                if cur > max_so_far:
                    max_so_far = cur
        table[w] = max_so_far
    print table    
    return table[W]

weight = [2,3,6,4]
cost = [3,4,6,10]
print knapsack(10,weight,cost)

