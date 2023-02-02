import random as r
number=r.randint(1,50)
print("What's your name?")
player_name=input("Please,enter your name ")

number_of_guess=0
while number_of_guess<5:
    guess=int(input("Enter your guess number="))
    number_of_guess+=1
    if guess< number:
        print("Your guess number is low.")
    elif guess>number:
        print("Your guess is too high.")
    elif guess==number:
        print("Your answer is right.")
        break
    else :
        print("You already tries for "+number_of_guess+" times.")
