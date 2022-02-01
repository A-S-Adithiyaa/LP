'''
In Bagels, a deductive logic game, you
must guess a secret three-digit number
based on clues. The game offers one of
the following hints in response to your guess:
“Pico” when your guess has a correct digit in the
wrong place, “Fermi” when your guess has a correct
digit in the correct place, and “Bagels” if your guess
has no correct digits. You have 10 tries to guess the
secret number.
'''


import random
import sys


while True:
    num = random.randint(100, 999)
    print(num)
    print("OK, i have thought of a number.\nTry guessing the number in 10 tries")
    for i in range(10):
        flag = 0
        num = str(num)
        print("\n\nGuess #" + str(i+1))
        guess = input("> ")

        if guess == num:
            print("You got it right!!!")
            break

        for n in guess:
            if n in num:
                if num.index(n) == guess.index(n):
                    print("Fermi", end="\t")
                else:
                    print("Pico", end="\t")
                flag = 1

        if not flag:
            print("Bagels", end="\t")

        if i == 9:
            print("\nYou have ran out of chances...")

    again = input("\nDo you want to play again? (y / n) : ")
    if again == "y":
        continue
    print("Thanks for playing\n")
    sys.exit(0)
