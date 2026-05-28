import random

print("🎯 Guess the Number Game!")
print("I'm thinking of a number between 1 and 100")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try higher 📈")
    elif guess > secret_number:
        print("Too high! Try lower 📉")
    else:
        print(f"Correct! 🎉 You guessed it in {attempts} attempts")
        break