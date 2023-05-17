import random
choice_list = ['rock','paper','scissors']
class Manual_RPS:

    def __init__(self):
        self.choice_list = choice_list
        
    def get_user_choice(self):
        while True:
           self.user_choice = input("Please choose either rock, paper or scissors  ").lower()
           if self.user_choice not in self.choice_list:
               print('Invalid choice.')
           else:
               print(f'You have chosen {self.user_choice}')
               break
                         
    def get_computer_choice(self):
        self.computer_choice = random.choice(choice_list)
        print(f'Computer has chosen {self.computer_choice}')
        return self.computer_choice
    
    def get_winner(self):
        if self.user_choice == self.computer_choice:
            print('It\'s a tie!')
        elif self.user_choice == 'rock':
            if self.computer_choice =='scissors':
                print('You win!')
            else:
                print('You lost')
        elif self.user_choice == 'paper':
            if self.computer_choice == 'rock':
                print('You won!')
            else:
                print('You lost')
        elif self.user_choice == 'scissors':
            if self.computer_choice == 'paper':
                print('You won!')
            else:
                print('You lost')
                                           
                                
play = Manual_RPS()
play.get_user_choice()
play.get_computer_choice()
play.get_winner()              

           

       

            
