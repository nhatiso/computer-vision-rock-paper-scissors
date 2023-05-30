from keras.models import load_model
import cv2
import numpy as np
import random
import time

model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
game_options = ["rock", "paper", "scissors"] 

with open ('labels.txt', 'r') as f:
    lines = f.readlines()
    labels = []
    for line in lines:
        labels.append (line.split (" ") [1].rstrip('\n' ))

class CameraRockPaperScissors:
    
    def __init__(self):
        self.game_options = game_options
        

        """ A function that initiates a 3 second countdown before the start of each round """
    def countdown(self): 
            start_time = time.time()
            number_count = 0
            while (time.time() - start_time) < 4:
                if round(time.time() - start_time) == 1 and number_count == 0:
                    number_count = 1
                    print(3) 
                elif round(time.time() - start_time) == 2 and number_count == 1: 
                    number_count = 2
                    print(2)
                elif round(time.time() - start_time) == 3 and number_count == 2: 
                    number_count = 3
                    print(1)
                elif round(time.time() - start_time) == 4 and number_count == 3: 
                    number_count = 4
                    print("Go!")
                elif number_count == 4:
                    break

            """ The function to establish a prediction choice using camera and a trained keras model """
    def get_prediction(self):        
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            prediction_choice = labels [np.argmax (prediction)]
            break
        return prediction_choice       
                    
        """ A function to determine the users choice by calling the get_prediction function """
    def get_user_choice(self):
        self.user_choice = self.get_prediction()
        while self.user_choice not in self.game_options:
            print("Invalid input! Please choose rock, paper or scisoors")
            self.user_choice = self.get_user_choice()   
        if self.user_choice == 0:
            self.user_choice = "rock"
        elif self.user_choice == 1:
            self.user_choice = "paper"
        elif self.user_choice == 2:
            self.user_choice= "scissors"
        return self.user_choice

        """ Function to determine  and return the result of each round. It takea the choices of the user and computer as arguments """
    def get_winner(self,computer_choice, user_choice):
        if self.user_choice == self.computer_choice:
            return "Tie"
        elif self.user_choice == "rock" and self.computer_choice == "scissors":
            return "User" 
        elif self.user_choice == "paper" and self.computer_choice == "rock":
            return "User"
        elif self.user_choice == "scissors" and self.computer_choice == "paper":
            return "User"
        else:
            return "Computer"
                        
            """ function to initiate the countdown and play the game over a specific winning score. It prints the game winner """       
    def play(self):
        user_wins = 0
        computer_wins= 0
        while computer_wins < 3 and user_wins < 3:
            input("\nPress Enter to play the round whenever you are ready ")
            self.countdown()
            self.user_choice = self.get_user_choice()
            self.computer_choice = random.choice(game_options)
            self.winner = self.get_winner(self.computer_choice,self.user_choice)
            if self.winner == "User":
                user_wins += 1
                print (f'You chose {self.user_choice}, Computer chose {self.computer_choice}')
                print (" You WON ! \n")
            elif self.winner == "Computer":
                computer_wins += 1
                print (f'You chose {self.user_choice}, Computer chose {self.computer_choice}')
                print (" The computer won. \n")
            else:
                print (f'You both chose {self.user_choice}')
                print('It\'s a tie! \n')
            print (f"Your score is: {user_wins}, The Computer's score is: {computer_wins}")
        if user_wins > computer_wins:
            print ("You are the WINNER, CONGRATULATIONS! \n\n")
        elif user_wins < computer_wins:
            print ("The Computer is the WINNER. \n\n")
        elif computer_wins == 3 or user_wins == 3:
            print(f"The {self.winner} won this game!\n") 
            cap.release()           # After the loop release the cap object - Ends image capture
            cv2.destroyAllWindows() # Destroy all the windows - Ends image capture
game = CameraRockPaperScissors()
game.play()



