import math

x = int(input())

result = 1 / (1 + math.pow(math.e, -x))

print(round(result, 2))