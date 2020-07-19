import math

angle = int(input())

radian = math.radians(angle)
ctg = (math.cos(radian) / math.sin(radian))
print(round(ctg, 10))