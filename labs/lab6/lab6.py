"""
Name: Harrison Penley
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("type your first and last name: ")
    s = name.split(" ")
    print(s[1] + ", " + s[0])

def company_name():
    domain = input("enter a website domain: ")
    s = domain.split(".")
    print(s[1])

def initials():
    n = eval(input("how many students are there?: "))
    for i in range(n):
        first = input("what is their first name?: ")
        last = input("what is their last name?: ")
        print(first[0] + last[0])

def names():
    name = input("enter a list of the names: ")
    name = name.split(", ")
    for i in name:
       initials = i.split(" ")
       print(initials[0][0] + initials[1][0])


def thirds():
    n = eval(input("how many sentences are there?: "))
    for _ in range(n):
        x = input("enter a sentence: ")
        third = x[2::3]
        print(third)

def word_average():
    x = input("enter a sentence: ")
    acc = 0
    words = x.split(" ")
    for word in words:
        length = len(word)
        acc = acc + length
    print(acc / len(words))

def pig_latin():
    x = input("enter a sentence: ")
    x.lower()
    words = x.split(" ")
    for word in words:
        piglatin = word[1:] + word[0] + "ay"
        print(piglatin, end=" ")

def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()


main()
