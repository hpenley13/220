"""
Name: Harrison Penley
lab11.py
"""


from random import *


def getwords(wordlist):
    infile = open(wordlist, "r")
    words = []
    for line in infile:
        words.append(line)
    return words


def pickword(words):
    randnum = randint(0, len(words))
    secret_word = words[randnum]
    return secret_word


def guessedword(secret_word, guessed_letters, guessed_word, turn_count, letter):
    letterlist = list(secret_word)
    for i in range(len(letterlist)):
        if secret_word[i] == letter:
            guessed_word[i] = letter
            return True
        else:
            turn_count = turn_count + 1
            guessed_letters.append(letter)
            return False


def wordspelled(guessed_word, secret_word):
    if guessed_word == secret_word:
        return True
    else:
        return False


def guessletter(guessed_letters, secret_word, guessed_word):
    letterguess = input("guess a letter: ")
    for i in range(len(secret_word)):
        if secret_word[i] == letterguess:
            guessed_word = guessed_word + letterguess
            return True
        else:
            guessed_letters = guessed_letters + letterguess
            return False


def printboard(guessed_word, turn_count, guessed_letters):
    print(guessed_word.join)
    print("number of wrong guesses:", turn_count)
    print("wrong letters guessed:", guessed_letters)


def playgame():
    turn_count = 0
    words = getwords("wordlist.txt")
    secret_word = pickword(words)
    guessed_word = len(secret_word) * "_"
    guessed_letters = []
    printboard(guessed_word, turn_count, guessed_letters)
    while turn_count < 7 and not wordspelled(guessed_word, secret_word):
        printboard(guessed_word, turn_count, guessed_letters)
        if guessletter(guessed_letters, secret_word, guessed_word):
            turn_count += 1
    if turn_count >= 7:
        print("game over, you lose")
    else:
        print("congratulations, you won")


def main():
    playgame()
    pass


main()
