import math

print("What do you want to calculate? months (n), annuity payment (a) or credit principal? (p)")
to_count = input("")

if to_count == "n":

    principal = int(input("Please enter your credit principal:"))
    payment = int(input("Please enter your monthly payment:"))
    interest = float(input("Please enter your credit interest in %:"))

    i = (interest / 100) / 12
    n = math.ceil(math.log((payment / (payment - i * principal)), 1 + i))
    years = n // 12
    months = n % 12
    if years != 0:
        if years == 1:
            if months == 1:
                print(f'You need {years} year and {months} month to repay this credit!')
            elif months == 0:
                print(f'You need {years} year to repay this credit!')
            else:
                print(f'You need {years} year and {months} months to repay this credit!')
        else:
            if months == 1:
                print(f'You need {years} years and {months} month to repay this credit!')
            elif months == 0:
                print(f'You need {years} years to repay this credit!')
            else:
                print(f'You need {years} years and {months} months to repay this credit!')
    else:
        if months == 1:
            print(f'You need {months} month to repay this credit!')
        elif months == 0:
            print(f'You\'re clear!')
        else:
            print(f'You need {months} months to repay this credit!')


elif to_count == "a":

    principal = int(input("Please enter your credit principal:"))
    period = int(input("Please enter duration of your credit in months:"))
    interest = float(input("Please enter your credit interest in %:"))
    i = (interest / 100) / 12

    payment = math.ceil(principal * ((i * math.pow((1 + i) , period) / (math.pow((1 + i) , period) - 1))))

    print(f'Your annuity payment = {payment}!')

elif to_count == "p":

    payment = float(input("Please enter your monthly payment:"))
    period = int(input("Please enter duration of your credit in months:"))
    interest = float(input("Please enter your credit interest in %:"))
    i = (interest / 100) / 12

    principal = (int) (payment / ((i * math.pow((1 + i) , period)) / (math.pow((1 + i) , period) - 1)))

    print(f'Your credit principal = {principal}!')

else:
    print("unknown command")

