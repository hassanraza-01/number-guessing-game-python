import random

print("🎯 Welcome to Number Guessing Game 🎯")

while True:
    secret_number = random.randint(1,100)
    attempts = 0
    max_attempts = 5
 
    print("\nI am thinking of a number between 1 and 100")
    print(f"You have {max_attempts} attempts")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠ Please enter a valid number!")
            continue

        if guess < 1 or guess > 100:
            print("⚠ Number must be between 1 and 100")
            continue

        attempts += 1
        
        if guess < secret_number:
            print("Too low! 📉")
        elif guess > secret_number:
            print("Too high! 📈")
        else:
            score = max_attempts - attempts + 1
            print(f"🎉 Correct! You guessed it in {attempts} attempts")
            print(f"🏆 Score: {score}")
            break
    
    else:
        print("❌ Game Over!")
        print(f"The number was {secret_number}")

    play = input("Play again? (y/n): ").lower()
    if play != 'y':
        print("Thanks for playing 👋")
        break
            
