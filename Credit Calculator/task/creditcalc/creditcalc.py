import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, choices=["annuity", "diff"], required=True)
parser.add_argument("--payment", type=float, required=False)
parser.add_argument("--principal", type=int, required=False)
parser.add_argument("--periods", type=int, required=False)
parser.add_argument("--interest", type=float, required=False)
args = parser.parse_args()

P = args.principal
n = args.periods
i = args.interest
monthly_payment = args.payment

#print(P)
#print(n)
#print(i)
#print(monthly_payment)

# errorrs
#if P != None and n != None and i == None:
#    print('Incorrect parameters.')
if args.type == None:
    print('Incorrect parameters.')

elif args.type == "diff":
    if i == None or P == None or n ==None:
        print('Incorrect parameters.')
    else:
        i = i / 100 / 12
        sum = 0
        for month in range(1, n + 1):
            D = math.ceil(P / n + i * (P - (P * (month - 1) / n)))
            sum = sum + D
            print(f'Month {month}: paid out {D}')
        overpayment = sum - P
        print()
        print(f'Overpayment = {overpayment}')


elif args.type == "annuity":

    if P and n and i:
        i = i / 100 / 12
        for month in range(1, n + 1):
            monthly_payment = math.ceil(P * (i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
        overpayment = int(n * monthly_payment - P)
        print(f'Your annuity payment = {monthly_payment}!')
        print(f'Overpayment = {overpayment}')

    elif monthly_payment and n and i:
        i = i / 100 / 12
        P = math.floor(monthly_payment / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1)))
        overpayment = int(n * monthly_payment - P)
        print(f'Your credit principal = {P}!')
        print(f'Overpayment = {overpayment}')

    elif P and monthly_payment and i:
        i = i / 100 / 12
        n = math.ceil(math.log(monthly_payment / (monthly_payment - i * P), 1 + i))
        if n < 12:
            n_str = str(n) + " months"
        elif n == 12:
            n_str = "1 year"
        elif n > 12 and n % 12 == 0:
            n_str = str(n // 12) + " years"
        else:
            n_str = str(n // 12) + " years and " + str(n % 12) + " months"
        overpayment = int(n * monthly_payment - P)
        print(f'You need {n_str} to repay this credit!')
        print(f'Overpayment = {overpayment}')

    elif P and n and i == None:
        print('Incorrect parameters.')

    elif monthly_payment and n and i == None:
        print('Incorrect parameters.')

    elif P and monthly_payment and i == None:
        print('Incorrect parameters.')

