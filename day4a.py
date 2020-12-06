import re

lines = open('input-day4.txt').read().split('\n')

i = 0
passports = []
passport = []
for x in lines:
    if not lines[i]:
        passports.append(passport[:])
        passport = []
        i += 1
        continue
    passport.append(lines[i])
    i += 1

valid1 = ['pid', 'cid', 'hgt', 'byr', 'ecl', 'eyr', 'iyr', 'hcl']
valid2 = ['pid', 'hgt', 'byr', 'ecl', 'eyr', 'iyr', 'hcl']
prelim_valids = []
for p in passports:
    pstr = " ".join(p)
    d = dict(s.split(':') for s in pstr.split(' '))
    if (set(d.keys()) == set(valid1)) or (set(d.keys()) == set(valid2)):
        prelim_valids.append(d)

valid_count = 0
for p in prelim_valids:
    p_valid = [False]*7
    for i in p.items():
        if (i[0] == 'pid'):
            result = re.match('^\d{9}$', i[1])
            if result:
                p_valid[0] = True
                print 'pid ', i[1], 'valid'
            else:
                print 'pid ', i[1], 'INVALID'
        elif (i[0] == 'hgt'):
            result = re.match('^(\d{2,3})(in|cm)$', i[1])
            if result:
                num = int(result.groups()[0])
                measure = result.groups()[1]
                if measure == 'in' and (num >= 59 and num <= 76):
                    print 'hgt ', num, measure, 'valid'
                    p_valid[1] = True
                elif measure == 'cm' and (num >= 150 and num <= 193):
                    print 'hgt ', num, measure, 'valid'
                    p_valid[1] = True
                else:
                    print 'hgt ', num, measure, 'INVALID'
        elif (i[0] == 'byr'):
            result = re.match('^(\d{4})$', i[1])
            if result:
                yr = int(result.groups()[0])
                if (yr >= 1920 and yr <= 2002):
                    print 'byr ', yr, 'valid'
                    p_valid[2] = True
                else:
                    print 'byr ', yr, 'INVALID'
        elif (i[0] == 'ecl'):
            result = re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', i[1])
            if result:
                p_valid[3] = True
                print 'ecl ', i[1], 'valid'
            else:
                print 'ecl ', i[1], 'INVALID'
        elif (i[0] == 'eyr'):
            result = re.match('^(\d{4})$', i[1])
            if result:
                yr = int(result.groups()[0])
                if (yr >= 2020 and yr <= 2030):
                    print 'eyr ', yr, 'valid'
                    p_valid[4] = True
                else:
                    print 'eyr ', yr, 'INVALID'
        elif (i[0] == 'iyr'):
            result = re.match('^(\d{4})$', i[1])
            if result:
                yr = int(result.groups()[0])
                if (yr >= 2010 and yr <= 2020):
                    print 'iyr ', yr, 'valid'
                    p_valid[5] = True
                else:
                    print 'iyr ', yr, 'INVALID'
        elif (i[0] == 'hcl'):
            result = re.match('^#([A-Fa-f0-9]{6})$', i[1])
            if result:
                p_valid[6] = True
                print 'ecl ', i[1], 'valid'
            else:
                print 'ecl ', i[1], 'INVALID'

    if (set(p_valid) == set([True]*7)):
        valid_count += 1


print "Pre-validation valids: ", len(prelim_valids)
print "Valid: ", valid_count
