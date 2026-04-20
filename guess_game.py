import random

Min: int = int(input("Enter Minimum Number: "))
Max: int = int(input("Enter Maximum Number: "))

secret: int = random.randint(Min, Max)
attempt: int = 0

while True:
    try:
        guess: int = int(input(f"Enter Guess Number ({Min}-{Max}): "))

        if not (Min <= guess <= Max):
            print(f"Please enter a number from {Min} to {Max}.")
            continue

        attempt += 1

        if guess == secret:
            print(f"🎯 You got it right in {attempt} attempt(s)!")
            break
        elif guess > secret:
            print("Too high! Go lower.")
        else:
            print("Too low! Go higher.")

    except ValueError:
        print("Enter numbers only.")
