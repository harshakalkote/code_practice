from math import log, ceil, floor
def check_kth_power(n, k):
        kth_log = log(n, k)
        return k ** int(ceil(kth_log)) == n or k ** int(floor(kth_log)) == n
       
print check_kth_power(12, 5)
