def bit_diff(n1,n2):
    cmn_d = n1 & n2
    all_d = n1 | n2
    diff = all_d - cmn_d
    cnt = 0
    while diff:
        if diff & 1:
            cnt+=1
        diff>>=1
    return cnt

print bit_diff(1,2)
