#import modules
import random

#options for the game
options = ['rock', 'paper', 'scissors']
answer = (random.choice(options))
print(answer)
#start the game
print("Welcome to Rock Paper Scissors!")
user_choice= input("Type in your choice:")



if user_choice ==  answer: 
    print("It's a draw!")
elif user_choice == 'scissors' and answer == 'paper': 
    print ('You won!')
elif user_choice == 'rock' and answer == 'scissors': 
    print  ('You won!') 
elif user_choice == 'paper' and answer == 'rock':
    print  ('You won!') 
else : 
    print ('Sorry, you loose!') 