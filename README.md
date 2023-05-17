### Computer Vision RPS

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock. The player who shows the first option that beats the other player's option wins. This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

## Milestone 2
The computer-vision-rock-paper-scissors uses an image project model with four different classes namely: Rock, Paper, Scissors, Nothing. The rock is represented by a fist, the paper is represented by an open palm, scissors is represented by two raised fingers while nothing is represented by no symbol or action. Teachable-Machine technology is used where images for each option are taken and then trained. To increase the model accuracy, several images of each class are taken from diffenet directions. Once satisfied with the model, the model is downloaded through the 'Tensorflow' tab containing the labels.txt and keras_model.h5 files.

## Milestone 3
A new virtual environment is created and appropriate libraries that work with the model are installed. The libraries rwquired for this model are opencv-python, tensorflow ad ipykernel. Once installation of the dependencies is complete, a requirements.txt file is created by running the command: pip list > requirements.txt. The requirements.txt file will enable any other person using the computer to install the exact dependences by running the command: pip install requirements.txt

## Milestone 4
A new python file named manual_rps is created where the code to play the rock paper scissors game between a computer and a player is developed. As more than two functions are used to make up the code for the game, a  python class named Manual_RPS is used. The game is centred around three choices namely: rock, paper, scissors. To enable the computer to make random choices, the random module is imported into the code. After initialising the choice_list variable, the get_user_choice function is defined to prompt the player to choose a choice using the built-in 'input' function. The user input is converted to lower case to match the lower case used in the choice_list variable. Should the player's input not in the choice_list, the while loop will reject it and request a new iput, otherwise the function prints and returns the choice. The choice is stored in a variable called player_choice.

<img width="714" alt="Screenshot 2023-05-17 at 11 46 41" src="https://github.com/nhatiso/computer-vision-rock-paper-scissors/assets/128712936/89318c58-d1ab-4d56-82ad-ee684282f4aa">

The get_computer_choice function is then defined and the random module is used to make a choice from the word_list and stored in a variable called computer_choice.This function also prints the computer choice.

<img width="417" alt="Screenshot 2023-05-17 at 12 01 54" src="https://github.com/nhatiso/computer-vision-rock-paper-scissors/assets/128712936/83f1466e-3427-4b87-a9b6-753d81d289f1">

To establish the winner, a get_winner function is defined. Several if-elif-else statements are created to so that a clear winner of the game is ascertained. The function also prints the outcome, 'You win', 'You lost', 'It's a tie'.

<img width="375" alt="Screenshot 2023-05-17 at 12 09 21" src="https://github.com/nhatiso/computer-vision-rock-paper-scissors/assets/128712936/15741ff4-8dcc-4283-9762-6377b99216a6">

To run the whole code together, the class variable by the name play is assigned. The three instances of the class are then called.

<img width="347" alt="Screenshot 2023-05-17 at 13 14 42" src="https://github.com/nhatiso/computer-vision-rock-paper-scissors/assets/128712936/2a2f0062-246c-489d-a7fa-c42db5647368">


