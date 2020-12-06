lines = open('input-day2.txt').read().split('\n')
lines[:] = [x for x in lines if x]
valid_pwd_count = 0
for x in lines:
    (poss, let, pwd) = x.split(' ')
    (pos1, pos2) = poss.split('-')
    pos1 = int(pos1)
    pos2 = int(pos2)
    let = let[0]
    pos = 1
    pos1Found = False
    pos2Found = False
    for y in list(pwd):
        if (y == let) and (pos == pos1):
            pos1Found = True
        elif (y == let) and (pos == pos2):
            pos2Found = True
        pos += 1

    if pos1Found != pos2Found:
        print 'VALID: pos=', pos-1, ' - ', x 
        valid_pwd_count += 1


print 'Valid count: ', valid_pwd_count
