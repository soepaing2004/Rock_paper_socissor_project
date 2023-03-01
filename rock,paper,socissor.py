import sys as s
import random as r
choices=['rock','paper','socissor']
computer=r.choice(choices)
player_score=0
computer_score=0

while True:
    player=input("If you want to close the game enter 'end'."+"\n"+"Enter your choice."+"\n"+"'rock,paper or socissor: ")
    if player.lower()==computer:
        print("Tie.")

    elif player.lower()=='rock':
        if computer=='paper':
            print("You lose.")
            computer_score+=1
            print("Computer score is ",computer_score)
        else :
            print("You win.")
            player_score+=1
            print("Your score is ",player_score)

    elif player.lower()=='paper':
        if computer=='socissor':
            print("You lose")
            computer_score+=1
            print("Computer score is ",computer_score)
        else :
            print("You win.")
            player_score+=1
            print("Your score is ",player_score)

    elif player.lower()=='socissor':
        if computer=='rock':
            print("You lose")
            computer_score+=1
            print("Computer score is ",computer_score)
        else :
            print("You win.")
            player_score+=1
            print("Your score is ",player_score)

    elif player.lower()=='end':
        if computer_score>player_score:
            print("You lose the game.The game is over.")
            break
        else :
            print("You win the game .The game is over.")
            break

    else :
        print("Please,select the valid option.")
s.exit("End of program.")