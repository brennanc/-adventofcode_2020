lines = open('input-day3.txt').read().split('\n')
lines[:] = [x for x in lines if x]
line_len = len(lines[0])
input_len = len(lines)

num_chars_needed_to_reach_right = input_len * 3
horizontal_copies = (num_chars_needed_to_reach_right / line_len)+1

#print "num_chars_needed_to_reach_right = ", num_chars_needed_to_reach_right 
#print "horizontal copies = ", horizontal_copies

i = 0
for x in lines:
    lines[i] = x*horizontal_copies
    i += 1

hit_tree_count = 0
x_idx=0
y_idx=0
while y_idx < len(lines)-1:
    x_idx += 3
    y_idx += 1
#    print "x_idx=",x_idx,"; y_idx=",y_idx

    if (lines[y_idx][x_idx] == '#'):
        hit_tree_count += 1
#        print 'lines[',y_idx,'][',x_idx,'] = ', lines[y_idx][x_idx]
#        print 'before lines[',y_idx,']', lines[y_idx]
        lines[y_idx] = lines[y_idx][:x_idx]+'X'+lines[y_idx][x_idx+1:]
#        print 'after  lines[',y_idx,']', lines[y_idx]
    else:
#        print 'lines[',y_idx,'][',x_idx,'] = ', lines[y_idx][x_idx]
#        print 'before lines[',y_idx,']', lines[y_idx]
        lines[y_idx] = lines[y_idx][:x_idx]+'O'+lines[y_idx][x_idx+1:]
#        print 'after  lines[',y_idx,']', lines[y_idx]

#for x in lines:
#    print x

print "Hit trees:", hit_tree_count
