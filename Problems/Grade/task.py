score = int(input())
max = int(input())

percentage = score / max

if percentage < 0.6:
    print ("F")
elif percentage < 0.7:
    print ("D")
elif percentage < 0.8:
    print ("C")
elif percentage < 0.9:
    print ("B")
else:
    print("A")
