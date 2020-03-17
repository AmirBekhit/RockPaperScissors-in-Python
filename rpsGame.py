# This is a simple game that my son was playing the other day and when we were playing when we were kids , at least most of us :)

import random
import sys
print('ROCK , paper, scissors')

# These variables keep track of the number of wins , losses and ties.
wins = 0
losses = 0
ties = 0

while True:
    # the %S is a placeholder , nothing more.
    print('%s Wins, %s Losses, %s Tie ' % (wins, losses, ties))
    while True:
        # The player enters his move
        print('PLEASE ENTER YOUR MOVE : (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # quitting the program
        if playerMove == "r" or playerMove == "s" or playerMove == "p":
            break  # getting out of the loop and jumping to next code block
        # this in case user entered any other letter , it will redirect him to the start of the loop
        print('Type one of the letters : r, p , s or q ONLY!')

    # Display the player's choice:
    if playerMove == 'r':
        print('ROCK versus ...')
    elif playerMove == 'p':
        print('PAPER versus ...')
    elif playerMove == 's':
        print('SCISSORS versus ...')

    # Display the computer's choice:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You loose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You loose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You loose!')
        losses = losses + 1
