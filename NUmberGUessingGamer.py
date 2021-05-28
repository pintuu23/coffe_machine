import random
n=random.randint(1,100)


def easy():
    count = 1
    guess_chance=10
    while 1 <= guess_chance:
        num=int(input("Guess the number: "))
        if num>n:
            print("Your guess was too high : Guess a number lower than", num)
        elif num <n:
            print("Your guess is too low : Guess a numebr higher than ", num)
        else:
            print("You win !")
            print(count,"Guesses you took")
            break
        guess_chance-=1
        print(guess_chance," Guesses left")
        count+=1
        print()
    print("GAME OVER")
    print("Number is ",n)

def hard():
    count = 1
    guess_chance=5
    while 1 <= guess_chance:
        num=int(input("Guess the number: "))
        if num>n:
            print("Your guess was too high : Guess a number lower than", num)
        elif num <n:
            print("Your guess is too low : Guess a numebr higher than ", num)
        else:
            print("You win !")
            print(count,"Guesses you took")
            break
        guess_chance-=1
        print(guess_chance," Guesses left")
        count+=1
        print()
    print("GAME OVER")
    print("Number is ",n)
game_level=input("What type of game you want ? easy or hard ")
if game_level=="easy":
    easy()
else:
    hard()