"""3.8 猜数字"""

import random


def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("I am thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low")
            elif guess > secret_number:
                print("Too high")
            else:
                print("Congratulations, you guessed it right!"
                      " You spent %d attempts." % attempts)
                break

        except ValueError:
            print("Enter a number between 1 and 100.")


if __name__ == "__main__":
    guess_number()
