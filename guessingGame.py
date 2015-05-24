from random import randint

def randomize():
    global target
    target = randint(1,50)

def gameLoop():
    guess = float(raw_input("Guess a number between 1 and 50: "))
    if guess == target:
        print "good"
        playAgain()
    elif guess > target:
        print "lower"
        gameLoop()
    elif guess < target:
        print "higher"
        gameLoop()

def game():
    """This is a short guessing game
    I am writing just to keep my python
    skills sharp."""
    
    randomize()
    gameLoop()

def playAgain():
    replies = ['yes', 'y', 'no', 'n']
    ask = str(raw_input("Would you like to play again?\n"))
    if ask.lower() == "yes" or ask.lower()== "y":
        game()
    elif ask.lower() == "no" or ask.lower() == "n":
        print "What ever, you a lameo anyway!"
        pass
    elif ask.lower() != replies:
        print "Yes or No?\n"
        playAgain()

game()
