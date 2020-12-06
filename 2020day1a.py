lines = open('day1-input.txt').read().split('\n')
lines[:] = [x for x in lines if x]
for x in lines:
  for y in lines:
    if (int(x)+int(y) == 2020):
	print x, y, int(x)+int(y), int(x)*int(y)
        quit()
