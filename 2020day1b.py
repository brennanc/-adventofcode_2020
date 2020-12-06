lines = open('day1-input.txt').read().split('\n')
lines[:] = [x for x in lines if x]
for x in lines:
  for y in lines:
    for z in lines:
        if (int(x)+int(y)+int(z) == 2020):
            print x, y, z, int(x)+int(y)+int(z), int(x)*int(y)*int(z)
            quit()
