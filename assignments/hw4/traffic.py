"""
Name: Harrison Penley
traffic.py

Problem: suffer innumerably because you can't round strings and floats break the entire code

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    roads = eval(input("how many roads were surveyed?: "))
    acc1 = 0
    total = 0

    for _ in range(roads):
        days = eval(input("how many days of survey were there for this road?: "))
        for _ in range(days):
            cars = eval(input("how many cars were there on each day?: "))
            acc1 = acc1 + cars
        average = acc1 / days
        print("average number of of vehicles that day:", (round(average, 2)))
        total += acc1
        acc1 = 0
    print("the total number of cars to travel on the roads surveyed:", (round(total, 2)))
    totalaverage = total / roads
    print("the average number of vehicles per road is:", (round(totalaverage, 2)))


if __name__ == "__main__":
    main()
