count = 0
repeat = 0
number = " "
while number != ".":
    number = input()
    if number == ".":
        break
    numberint = int(number)
    count = count + numberint
    repeat += 1

print(count / repeat)