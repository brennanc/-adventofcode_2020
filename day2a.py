lines = open('input-day2.txt').read().split('\n')
lines[:] = [x for x in lines if x]
valid_pwd_count = 0
for x in lines:
    (occs, let, pwd) = x.split(' ')
    (occmin, occmax) = occs.split('-')
    occmin = int(occmin)
    occmax = int(occmax)
    let = let[0]
    count = 0
    for y in list(pwd):
        if (y == let):
            count = count+1

    if (count >= occmin) and (count <= occmax):
        print 'VALID: ', x
        valid_pwd_count = valid_pwd_count + 1


print 'Valid count: ', valid_pwd_count
