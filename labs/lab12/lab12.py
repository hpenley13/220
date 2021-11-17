"""
Name: Harrison Penley
lab12.py
"""


from random import randint


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "Harrison Penley"
    except:
        pass


def read_data(filename):
    f = open(filename, "r")
    d = f.readlines()
    d = d[0].split(" ")
    i = 0
    while i < len(d):
        d[i] = int(d[i])
        i += 1
    return d


def is_in_linear(value, lst):
    i = 0
    while i < len(lst):
        if lst[i] == value:
            return True
        i += 1

    return False



def good_input():
    x = eval(input("enter a number between 1 and 10: "))
    while x > 10 or x < 1:
        x = eval(input("input wasn't in the range 1-10, try entering again."))
    return x


def num_digits():
    x = eval(input("enter a positive integer: "))
    while x >= 1:
        i = 0
        while x > 0:
            i += 1
            x //= 10
        print("number of digits:", i)
        x = eval(input("enter a positive integer again: "))


def hi_lo_game():
    number = randint(1, 100)
    x = eval(input("take a guess at the number between 1-100: "))
    guesses = 0
    while x != number and guesses < 7:
        if x > number and guesses != 6:
            print("the number was too high")
            x = eval(input("guess again"))
        elif x < number and guesses != 6:
            print("the number was too low")
            x = eval(input("guess again"))
        guesses += 1
    if x == number:
        print("you've won and guessed correctly in", guesses, "guesses!")
    else:
        print("sorry, you lost, the correct number was", number)


def main():
    d = read_data("dataSorted.txt")
    print(is_in_linear(5, d))
    find_and_remove_first([1, 2, 3, 4, 5], 2)
    good_input()
    num_digits()
    hi_lo_game()
    pass


main()
