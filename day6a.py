lines = open('input-day6.txt').read().split('\n')

group = 0
ppl = 0

j = 0
yes = set()
tot_yes = 0
while j < len(lines):
    c = lines[j]
    if not c.strip():
        print j, ' blank'
        print group, '-', len(yes)
        tot_yes += len(yes)
        yes = set()
        group += 1
    else:
        for y in c:
            yes.add(y)
    j += 1

print tot_yes
