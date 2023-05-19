import random
choice_list = ['rock','paper','scissors']

def get_computer_choice():
    computer_choice = random.choice(choice_list)
    return computer_choice

def get_player_choice():
    user_choice = input(" Please choose rock,paper or scissors: ").lower()
    while user_choice not in choice_list:
        print(" Wrong input, Please try again.\n")
        user_choice = get_player_choice()
    return user_choice

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "Player" 
    elif user_choice == "paper" and computer_choice == "rock":
       return "Player"
    elif user_choice == "scissors" and computer_choice == "paper":
       return "Player"
    else:
       return "Computer"

def play():
    player_score = 0
    computer_score = 0
    for attempts in range(1,2):
        user_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = get_winner(user_choice,computer_choice)
        if winner == "Player":
            player_score += 1
            print (f'You chose {user_choice}, Computer chose {computer_choice}')
            print (" You WON ! \n")
        elif winner == "Computer":
            computer_score += 1
            print (f'You chose {user_choice}, Computer chose {computer_choice}')
            print (" The computer won. \n")
        else:
            print (f'You both chose {user_choice}')
            print('It\'s a tie! \n')
        print (f"Your score was: {player_score}, The Computer's score was: {computer_score}")
    if player_score > computer_score:
        print ("You are the WINNER, CONGRATULATIONS! \n\n")
    elif player_score < computer_score:
        print ("The Computer is the WINNER. \n\n")
    else:
        print('It\'s a Tie!')    

play()

           

       

            
