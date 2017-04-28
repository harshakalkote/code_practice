def find_replaceable_element(arr, n):
    max_sum = [0] * len(arr)
    lowest = [-10000] * len(arr)
    current_sum = 0
    for index, val in enumerate(arr):
        current_sum += val
        max_sum[index] = max(current_sum, val)
        if index >= 1:
            if lowest[index-1] > val:
                lowest[index] = val
            else:
                lowest[index] = lowest[index-1]
        else:
            lowest[index] = val
            
        if val > current_sum:
            current_sum = val
            lowest[index] = val
            
    max_got = 0
    l =0
    
    for i, val in enumerate(max_sum):
        cur_max = max_sum[i] - lowest[i] + n
        if max_got < cur_max:
            max_got = cur_max
            l = lowest[i]
    return l, max_got
        
 

arr = [1, 2, 10, -3, -10, 8, 5]
print find_replaceable_element(arr, 8)    
