number = int(input())

if number > 1:
    for i in range(2, number + 1):
        if i == number:
            print("This number is prime")
            break
        if number % i == 0:
            print("This number is not prime")
            break
else:
    print("This number is not prime")