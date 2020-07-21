# put your python code here
a = int(input())
b = int(input())

s = 0
divisor = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        s = s + i
        divisor = divisor + 1
    else:
        pass

print(s / divisor)