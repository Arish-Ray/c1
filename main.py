import random
num = random.randint(1,10)
print("welcome to the 'guess a number' game")
print("rules : i shall think of a number 1,10 and you should guess it")
count = 0
while True :
    count = count+1
    guess = int(input("enter your guess:"))
    if guess > num:
        print("oops!your guess is bigger")
    elif guess < num:
        print("oops!your guess is smaller")
    elif guess == num:
        print("you guessed it correct!")
        print("you have taken",count," turns.")
        break 
    else :
        print("invalid value")
