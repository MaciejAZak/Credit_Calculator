X = int(input())
Y = int(input())

if X == 1 or X == 8:
    if Y == 1 or Y == 8:
        print("3")
    else:
        print("5")
else:
    if Y == 1 or Y == 8:
        print("5")
    else:
        print("8")