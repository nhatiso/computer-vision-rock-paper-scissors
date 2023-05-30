### Computer Vision RPS

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Milestone 2
 The computer-vision-rock-paper-scissors uses an image project model with four different classes namely: Rock, Paper, Scissors, Nothing. The rock is represented by a fist, the paper is represented by an open palm, scissors is represented by two raised fingers while nothing is represented by no symbol or action. Teachable-Machine technology is used where images for each option are taken and then trained. To increase the model accuracy, several images of each class are taken from diffenet directions. Once satisfied with the model, the model is downloaded through the 'Tensorflow' tab containing the labels.txt and keras_model.h5 files.

 ## Milestone 3
 A new virtual environment is created and appropriate libraries that work with the model are installed. The libraries rwquired for this model are opencv-python, tensorflow ad ipykernel. Once installation of the dependencies is complete, a requirements.txt file is created by running the command: pip list > requirements.txt. The requirements.txt file will enable any other person using the computer to install the exact dependences by running the command: pip install requirements.txt

 ## Milestone 4
 A new python file named manual_rps is created where the code to play the rock paper scissors game between a computer and a player is developed. As more than two functions are used to make up the code for the game, a  python class named Manual_RPS is used. The game is centred around three choices namely: rock, paper, scissors. To enable the computer to make random choices, the random module is imported into the code. After initialising the choice_list variable, the get_user_choice function is defined to prompt the player to choose a choice using the built-in 'input' function. The user input is converted to lower case to match the lower case used in the choice_list variable. Should the player's input not in the choice_list, the while loop will reject it and request a new iput, otherwise the function prints and returns the choice. The choice is stored in a variable called player_choice.

 The get_computer_choice function is then defined and the random module is used to make a choice from the word_list and stored in a variable called computer_choice.This function also prints the computer choice.

 To establish the winner, a get_winner function is defined. Several if-elif-else statements are created to so that a clear winner of the game is ascertained. The function also prints the outcome, 'You win', 'You lost', 'It's a tie'.

 To run the whole code together, the class variable by the name play is assigned. The three instances of the class are then called.

 ## Milestone 5
 Code for the game has been created using the class called CameraRockPaperScissors. The get_prediction function is used to capture and return the closest possible prediction of the user's action between rock, paper or scissors.
 The get_user_choice function then make use of the returned value from the get_prediction function to create and return the user_choice. A while loop is used to check for valid user input in case 'nothing' is provided by the user.
 The get_winner function determines the winner of a round by taking in user_choice and computer_choice as arguments. The computer_choice variable is obtained by the use if imported random module to choose between rock, paper and scissors. The use of random module reduces any computer choice biases when playing the game. Should the user and computer choose the same action, a "Tie" is returned, otherwise either "User" or "Computer" is returned.
 A countdown function is created so that there is a three second countdown before the start of every round. To effectively code the countdown function, the time module is imported and the start_time variable is set to time.time(). The countdown is also printed to prompt the user to start playing.
 The play function is coded so that the game is played. The user_wins and computer_wins variables are initially set to zero. A while loop is used to set the winning total score. Inside this while loop, the user press 'Enter' to start the game. Once the the winning score has been attained, the function prints the winner.

