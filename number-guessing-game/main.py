from random import randint
def game_easy(rand):
    count=0
    attempt=5
    guess = int(input("Guess a number between 1 and 10: "))
    while True:
        count+=1
        attempt -= 1

        if rand>guess:
            print("Too low!")
        elif rand<guess:
            print("Too high!")

        else:
            if count ==1:
                print(f" you guessed right no. in {count} move!")
            else:
                print(f" you guessed right no. in {count} moves!")

            return 5

        if attempt ==0 :
            lose_message = f"Out of attempts Correct no is {rand}"
            print(lose_message)
            return 0

        guess = int(input("Guess a number between 1 and 10: "))

def game_medium(rand):
    count=0
    attempt=3
    guess = int(input("Guess a number between 1 and 10: "))
    while True:
        count+=1
        attempt -= 1

        if rand>guess:
            print("Too low!")
        elif rand<guess:
            print("Too high!")

        else:
            if count ==1:
                print(f" you guessed right no. in {count} move!")
            else:
                print(f" you guessed right no. in {count} moves!")

            return 10

        if attempt ==0 :
            lose_message = f"Out of attempts Correct no is {rand}"
            print(lose_message)
            return 0

        guess = int(input("Guess a number between 1 and 10: "))

def game_hard(rand):
    count=0
    attempt=1
    guess = int(input("Guess a number between 1 and 10: "))
    while True:
        count+=1
        attempt -= 1
        if rand>guess:
            print("Too low!")
        elif rand<guess:
            print("Too high!")

        else:
            if count ==1:
                print(f" you guessed right no. in {count} move!")
            else:
                print(f" you guessed right no. in {count} moves!")

            return 20

        if attempt ==0 :
            lose_message = f"Out of attempts Correct no is {rand}"
            print(lose_message)
            return 0

        guess = int(input("Guess a number between 1 and 10: "))

score=0
while True:

  print("Welcome to number guessing game")
  print("Please Choose Difficulty")
  print("1. Easy (5 attempts)")
  print("2. Medium (3 attempts)")
  print("3. Hard (1 attempt)")
  a=int(input("Enter your choice: "))

  if a==1:
      rand = randint(1, 10)
      a=game_easy(rand)
      score+=a
      print(f"Current Score : {score}")

  elif a==2:
      rand = randint(1, 10)
      b = game_medium(rand)
      score += b
      print(f"Current Score : {score}")

  elif a==3:
      rand = randint(1, 10)
      c = game_hard(rand)
      score += c
      print(f"Current Score : {score}")

  else:
      print("Invalid Choice")


  b = input("Wanna Play Again? (y/n): ").lower()

  while b != "y" and b != "n":
       print("Invalid Choice! Please enter y or n.")
       b = input("Wanna Play Again? (y/n): ").lower()

  if b == "n":
    print("Thank you for playing")
    print(f"Your Final Score is {score}")
    break


