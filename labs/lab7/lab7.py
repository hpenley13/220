"""
Name: Harrison Penley

Lab7.py
"""


def cash_conversion():
    x = eval(input("how many dollars you got?: "))
    print('${:.2f}'.format(x))

def encode():
    st = input("what do you want to encode?: ")
    key = eval(input("whats the key number?: "))
    acc = " "
    for c in st:
        x = ord(c)
        x = x + key
        acc = acc + chr(x)
    print(acc)

def sphere_area(radius):
    A = 4 * 3.14 * (radius ** 2)
    return A

def sphere_volume(radius):
    V = (4 / 3) * 3.14 * (radius ** 3)
    return V

def sum_n(n):
    acc = 0
    for i in range(n):
        acc = acc + i
    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + (i ** 3)
    return acc

def encode_better():
    s = input("what is the string to be encoded?: ")
    k = input("what is the key?: ")
    acc = " "
    for i in range(len(s)):
        c = s[i]
        key = k[i]
        key = ord(key) - 97
        c = ord(c) + key
        acc = acc + chr(c)
    print(acc)



def main():
    cash_conversion()
    encode()
    sphere_area(3)
    print(sphere_area(3))
    sphere_volume(2)
    print(sphere_volume(2))
    sum_n(5)
    print(sum_n(5))
    sum_n_cubes(5)
    print(sum_n_cubes(5))
    encode_better()
    pass


main()
