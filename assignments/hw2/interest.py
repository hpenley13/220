"""
Harrison Penley
interest.py

Problem: create a program that can solve for accrued interest over time
"""


def main():
    rate = eval(input("input the annual interest rate: "))
    decimalrate = rate / 100
    days = eval(input("input the number of days in the billing cycle: "))
    previous = eval(input("input the previous net balance of the account: "))
    payment = eval(input("input the payment amount: "))
    day_paid = eval(input("input the day of the month in which the payment was made: "))
    step1 = previous * days
    step2 = payment * (days - day_paid)
    step3 = step1 - step2
    dailybalance = step3 / days
    monthlyrate = decimalrate / 12
    monthly_interest = dailybalance * monthlyrate
    print(round(monthly_interest, 2))

if __name__ == "__main__":
    main()
