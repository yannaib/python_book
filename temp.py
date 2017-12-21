from random import randint
from easygui import integerbox, msgbox
msgbox ('Hello. I\'ll give you six tries to guess a number between 1 to 100.')
secret=randint (0, 100)
tries=0
guess=integerbox ('What\'s your guess?' , upperbound=100)
while (True):
    if tries>=6:
        msgbox ('Sorry, You had more than six tries.')
        msgbox ('The secret number was '+str(secret)+'.')
        break
    elif guess<secret:
        tries+=1
        guess=integerbox ('The secret number is higher than you think.'
                          '\nYou have '+str(7-tries)+' guesses left.'
                          '\nWhat\'s your guess?', upperbound=100)
    elif guess>secret:
        tries+=1
        guess=integerbox ('The secret number is lower than you think.'
                          '\nYou have '+str(7-tries)+' guesses left.'
                          '\nWhat\'s your guess?' , upperbound=100)
    elif guess==secret:
        msgbox ('Greetings! You found my secret!')
        msgbox('\nThe secret number was '+str(secret)+'.')
        break
