# proj 03: Guessing Game
#
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high,
# or exactly right. Keep the game going until the user types exit.
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
#
# """
congrats = 'Congrats! You won the game.'
high = 'Your number was too high, try again.'
low = 'Your number was too low, try again.'
guesses = int(3)
import random
rnum = random.randint(1,9)
print rnum


unum = int(raw_input('Pick a number '))
if unum == rnum:
    print congrats
    guesses = guesses - 3

elif unum < rnum:
    print low
    guesses = guesses - 1
    print ' '
    print 'you have'
    print  guesses
    print 'guesses left'

elif rnum < unum:
    print high
    guesses = guesses -1
    print ' '
    print 'you have'
    print  guesses
    print 'guesses left'


#2
    unum = int(raw_input('Pick a number '))
    if unum == rnum and guesses>0:
        print congrats
    elif unum < rnum:
        print low
        guesses = guesses - 1
        print ' '
        print 'you have'
        print  guesses
        print 'guesses left'
    elif rnum < unum:
        print high
        guesses = guesses -1
        print ' '
        print 'you have'
        print  guesses
        print 'guesses left'

#3
while guesses>0:
    unum = int(raw_input('Pick a number '))
    if unum == rnum and guesses>0:
        print congrats
    elif unum < rnum:
        print low
        guesses = guesses - 1
        print ' '
        print 'you have'
        print  guesses
        print 'guesses left'
    elif rnum < unum:
        print high
        guesses = guesses -1
        print ' '
        print 'you have'
        print  guesses
        print 'guesses left'


    #still a wip, need game to end if they win