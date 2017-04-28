def dice_rolls(ways, sum_to_get):
    dice_rolls_table = [[0] * (sum_to_get+1) for _ in xrange(ways+1)]
    #for j in xrange(7):
    dice_rolls_table[0][0] = 1
    for sub_ways in xrange(1, ways+1):
        for sub_sum in xrange(1, sum_to_get+1):
            for k in xrange(1, min(6,sub_sum)+1):
                dice_rolls_table[sub_ways][sub_sum] += dice_rolls_table[sub_ways-1][sub_sum-k]  
    print dice_rolls_table
    return dice_rolls_table[ways][sum_to_get]                
            
print dice_rolls(2,8)            


