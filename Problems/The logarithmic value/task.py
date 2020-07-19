import math

x = int(input())
y = int(input())
if y <= 0 or y == 1:
    print(round(math.log(x), 2 ))
else:
    print(round(math.log(x, y), 2))