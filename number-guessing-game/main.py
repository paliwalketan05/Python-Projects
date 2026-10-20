from random import randint
def game(rand):
    count=0
    attempt=5
    guess = int(input("Guess a number between 1 and 10: "))
    while True:
        count+=1
        attempt -= 1
        if attempt ==0 :
            lose_message = f"Out of attempts Correct no is {rand}"
            print(lose_message)
            return
        if rand>guess:
            print("Too low!")
        elif rand<guess:
            print("Too high!")

        else:
            if count ==1:
                print(f" you guessed right no. in {count} move!")
            else:
                print(f" you guessed right no. in {count} moves!")
            return
        guess = int(input("Guess a number between 1 and 10: "))

rand=randint(1,10)
game(rand)