secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("a number between 1 and 10: "))
    if guess == secret_number:
        print( Your guess is right!)
    elif guess > secret_number:
        print("your number is biger")
    else:
        print("your number is smaller")
