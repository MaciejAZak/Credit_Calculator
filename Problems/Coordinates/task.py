inputX = float(input())
inputY = float(input())

if inputX > 0:
    if inputY > 0:
        print("I")
    elif inputY < 0:
        print("IV")
elif inputX < 0:
    if inputY > 0:
        print("II")
    elif inputY < 0:
        print("III")