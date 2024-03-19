import random

# Create an app that generate a random value between rock, paper, scissors
# The app will also take a user input and compare it to the random value
# If the user input is the same as the random value it's a tie
# If the user input is invalid, the app will return an error message
# If the user input is different from the random value, calculate the winner assigning rock = 3, scissors = 2, paper = 1
# If the user input is screen the app will return the score
# The app will return the winner and the score
# The app will ak the user if they want to play again
# If the user input is yes, the app will generate a new random value
# If the user input is no, the app will show the final score and end the game
def generate_random_value():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def calculate_winner(user_input, random_value):
    if user_input == random_value:
        return 'tie'
    elif user_input == 'rock':
        if random_value == 'scissors':
            return 'user'
        else:
            return 'computer'
    elif user_input == 'paper':
        if random_value == 'rock':
            return 'user'
        else:
            return 'computer'
    elif user_input == 'scissors':
        if random_value == 'paper':
            return 'user'
        else:
            return 'computer'
    else:
        return 'error'

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        random_value = generate_random_value()
        user_input = input('Enter your choice (rock, paper, scissors, screen): ')

        if user_input == 'screen':
            print(f'Score: User - {user_score}, Computer - {computer_score}')
            continue

        winner = calculate_winner(user_input, random_value)

        if winner == 'tie':
            print('It\'s a tie!')
        elif winner == 'user':
            print('You win!')
            user_score += 1
        elif winner == 'computer':
            print('Computer wins!')
            computer_score += 1
        else:
            print('Invalid input!')

        play_again = input('Do you want to play again? (yes/no): ')
        if play_again == 'no':
            print(f'Final Score: User - {user_score}, Computer - {computer_score}')
            break

play_game()