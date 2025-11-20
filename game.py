import random

def guessing_game():
  """A simple number guessing game."""

  secret_number = random.randint(1, 100)
  guess = None

  print("I'm thinking of a number between 1 and 100.")

  while guess != secret_number:
    try:
      guess = int(input("What's your guess? "))

      if guess < secret_number:
        print("Too low!")
      elif guess > secret_number:
        print("Too high!")
      else:
        print("You got it! The number was", secret_number)
    except ValueError:
      print("Please enter a valid number.")

if __name__ == "__main__":
  guessing_game()
