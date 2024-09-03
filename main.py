import random

#function to roll die -> returns random value between 1-6 inclusive
def roll_die():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

#setting number of players from user input
while True:
    num_of_players = input('Set Number of Players: ')
    if num_of_players.isdigit():
        num_of_players = int(num_of_players)
        if 2 <= num_of_players <= 6:
            break
        else:
            print('Number of Players Must Be 2-4!')
    else:
        print('Invalid Input! Try again...')

#setting target score from user input
while True:
    target_score = input('Set Target Score: ')
    if target_score.isdigit():
        target_score = int(target_score)
        if target_score > 0:
            break
        else:
            print('Target Score Must Be Greater Than 0!')
    else:
        print('Invalid Input! Try again...')

#initializing scores list with 0 for each player
player_scores = [0 for _ in range(num_of_players)]

#game loop that simulates turns until a player reaches or exceeds the target score
while max(player_scores) < target_score:
    for player_index in player_scores:
        print('Player ' + str(player_index + 1) + '\'s turn...')
        turn_score = 0
        while True:
            player_choice = input('Enter \'R\' to roll die or \'E\' to end turn: ').lower()
            if player_choice == 'r':
                current_roll = roll_die()
                print('Player', player_index + 1, 'rolled', current_roll)
                if current_roll == 1:
                    turn_score = 0
                    print('Yikes! You lost your turn points.')
                    break
                turn_score += current_roll
            elif player_choice == 'e':
                break
            else:
                print('Invalid Input!')
            print('Player', player_index + 1, 'Turn Score:', turn_score)
        print('Player', player_index + 1, 'Total Score:', player_scores[player_index])