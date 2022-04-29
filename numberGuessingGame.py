import random


def guess():
    number = random.randint(1, 10)
    print("Enter a number between 1 to 10: ")
    print(number)
    while True:
        a = int(input("Guess the Number: "))
        if a == number:
            print("You win")
            break
        elif(a > 10 or a < 1):
            print("Number is between 1 to 10")
            continue
        else:
            print("Try again")
            continue

if __name__ == '__main__':
    guess()