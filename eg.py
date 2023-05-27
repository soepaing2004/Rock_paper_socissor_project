import random
choices=['rock','paper','socissor']
computer=random.choice(choices)
computer_score=0
player_score=0
player_input=input("Enter your option.")

def rock():
    while player_input.lower() == 'rock':
        if computer.lower() == 'paper':
            print("You lose.")
            computer_score=computer_score+1

        else:
            print("You win")
            player_score=player_score+1

def paper():
    while player_input == 'paper':
        if computer.lower() == 'socissor':
            print("You lose this time.")
        else:
            print("You win.")

def socissor():
    while player_input.lower() == 'socissor':
        if computer == 'rock':
            print("You lose")
        else:
            print("you win.")

def option():
    while True:
        player_input = input("Enter your option.")
        if player_score == 3:
            print("You win.")
            break

        elif computer_score == 3:
            print("You lose.Good luck for next time.The game is over.")
            break
        elif player_input == computer:
            print("tie")
        elif player_input.lower() == 'rock':
            rock()
        elif player_input.lower() == 'paper':
            paper()
        elif player_input == 'socissor':
            socissor()


