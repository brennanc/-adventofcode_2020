lines = open('input-day5.txt').read().split('\n')
lines[:] = [x for x in lines if x]
maxSeatID = 0
seat_ids = []
for x in lines:
    i = 0
    top = 127
    bot = 0
    row = 0
    column = 0
    while i < 7:
        mid = ((top - bot) / 2) + bot
        if x[i] == 'F':
            top = mid
        elif x[i] == 'B':
            bot = mid + 1
#        print  bot, " through", top
        i += 1
    row = bot if x[i-1] == 'F' else top

    top = 7
    bot = 0
    while i < 10:
        mid = ((top - bot) / 2) + bot
        if x[i] == 'L':
            top = mid
        elif x[i] == 'R':
            bot = mid + 1
#        print  bot, " through", top
        i += 1

    column = bot if x[i-1] == 'L' else top
    seatID = row * 8 + column
    seat_ids.append(int(seatID))

print "maxSeatID =", max(seat_ids)
seat_ids.sort()
i = 0
prev = None
while i < len(seat_ids):
    s = seat_ids[i]
    if (prev != None):
        if (s - prev) > 1:
            print "WARNING: seatId = ", s, " prev = ", prev
    prev = s
    i+=1

