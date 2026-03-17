import random
# Generate a random number between 1 and 100

number = random.randint(1,100)

attempts = 5 # maximum number of attempts

print(" Welcome to the number guessing game!")
print("guess a number beyween 1 and 100")
print("You have", attempts,"attempts")

for i in range(attempts):
    guess = int(input("Enter you guess:"))

    if guess == number:
     print("Congratulations! You guessed the number correctly. ")
     break

    elif guess > number:
       print("Too High!")

    elif guess < number:
       print("Too Low!")

       print("Attempts left:", attempts -i-1)

else:
   print("Game Over! The correct number was:", number)     
        



