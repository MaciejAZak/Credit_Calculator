credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
print("What's your credit principal")
credit_principal = int(input())
print("Periods (m) or Monthly Payment? (p)")
to_count = input("")

if to_count == "m":
    payment = int(input("Please enter your monthly payment:"))
    months = round(credit_principal / payment)
    if months == 1:
        print("{0} month".format(months))
    else:
        print("{0} months".format(months))
elif to_count == "p":
    periods = int(input("Please enter amount of periods:"))
    monthly_payment = round((credit_principal / periods) + 0.5, 0)
    last_payment = credit_principal - (periods - 1) * monthly_payment
    print("Your monthly payment = {0} with last payment = {1}".format(monthly_payment,last_payment))
else:
    print("unknown command")

