"""
Harrison Penley
mean.py

Problem: Solve for the RMS, Harmonic mean, and Geometric mean from user input values

Certification of Authenticity:
I certify that this assignment is entirely my own work

"""
# 1) the program will solve for the RMS, harmonic mean,
# and geometric mean using values acquired from the user.

# 2) the inputs will the number of values to find the mean,
# and the actual values listed.
# 2 cont.) the outputs will be the RMS, harmonic mean,
# and geometric mean solved for using the input values.

# 3) the program must ask for user input of the #
# of items to be in the sequence, then there needs to be a loop
# for the range of the input asking for
# individual values of each of the numbers.
# there will need to be 2 accumulators to be
# able to compile the sum and product of "xi"
# to use in the mean equations.
# then, the found sum and product will be used in the
# mean equations to solve for the RMS, harmonic mean,
# and geometric mean. These values will all be solved
# for and then printed back to the user as an output.


import math


def main():
    sequ = eval(input("enter the number of values to be entered: "))
    acc1 = 0
    acc2 = 1
    acc3 = 0
    acc4 = 0
    for i in range(sequ):
        values = eval(input("enter the value: "))
        acc1 = acc1 + values
        acc2 = acc2 * values
        acc3 = acc3 + values ** 2
        acc4 = acc4 + 1 / values
    rms = (math.sqrt(acc3 / sequ))
    harmonic = sequ / acc4
    geo = acc2 ** (1 / sequ)
    print(round(rms, 3))
    print(round(harmonic, 3))
    print(round(geo, 3))

if __name__ == "__main__":
    main()
