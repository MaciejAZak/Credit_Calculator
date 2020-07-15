money = int(input())
if money >= 6769:
    no_animals = money // 6769
    if no_animals > 1:
        print("{0} sheep".format(no_animals))
    else:
        print("{0} sheep".format(no_animals))
elif money >= 3848:
    no_animals = money // 3848
    if no_animals > 1:
        print("{0} cows".format(no_animals))
    else:
        print("{0} cow".format(no_animals))
elif money >= 1296:
    no_animals = money // 1296
    if no_animals > 1:
        print("{0} pigs".format(no_animals))
    else:
        print("{0} pig".format(no_animals))
elif money >= 678:
    no_animals = money // 678
    if no_animals > 1:
        print("{0} goats".format(no_animals))
    else:
        print("{0} goat".format(no_animals))
elif money >= 23:
    no_animals = money // 23
    if no_animals > 1:
        print("{0} chickens".format(no_animals))
    else:
        print("{0} chicken".format(no_animals))
else:
    print("None")