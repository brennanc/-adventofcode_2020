lines = open('input-day3.txt').read().split('\n')
lines[:] = [x for x in lines if x]
line_len = len(lines[0])
input_len = len(lines)


def tree_count(lines, right, down):
    hit_tree_count = 0
    x_idx=0
    y_idx=0
    while y_idx < len(lines)-1:
        x_idx += right
        y_idx += down

        if (lines[y_idx][x_idx] == '#'):
            hit_tree_count += 1
    return hit_tree_count

num_chars_needed_to_reach_right = input_len * 7 # because largest test case was 7
horizontal_copies = (num_chars_needed_to_reach_right / line_len)+1


i = 0
for x in lines:
    lines[i] = x*horizontal_copies
    i += 1

r1d1 = tree_count(lines, 1, 1)
r3d1 = tree_count(lines, 3, 1)
r5d1 = tree_count(lines, 5, 1)
r7d1 = tree_count(lines, 7, 1)
r1d2 = tree_count(lines, 1, 2)
print "magic number = ", r1d1*r3d1*r5d1*r7d1*r1d2
