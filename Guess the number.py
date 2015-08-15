
import simplegui
import math
import random


# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number=42
    range100()
    
    
    # initialize global variables used in your code here

    # remove this when you add your code    
    


# define event handlers for control panel
def range100():
    print 
    print "Starting new game"
    
    global secret_number
    secret_number= random.randrange(0,101)
   
    global count
    count = int(math.log(102, 2))
   
    print "Number is in range of 0 to 100"
    print "you have", count, "counts"
    
    

def range1000():
    print 
    print "Starting new game"
    
    
    global secret_number
    secret_number= random.randrange(0,1001)
   
    global count
    count=int(math.log(1002, 2))
    print "Number is in range of 0 to 1000"
    print "you have", count, "counts"
    
def you_lose():
        
        print "No more counts: You loose"
        global secret_number
        print "The  number was", secret_number
        new_game()
    
def input_guess(guess):
    guessed_number=int(guess)
    print "Guess was ", guessed_number
    # main game logic goes here	
    global count
    
    if guessed_number>secret_number:
        print "Lower"
        count -= 1
        if count==0:
            you_lose()
        print "Remaining counts:", count
    elif    guessed_number<secret_number: 
            print "Higher"
            count -= 1
            if count==0:
                    you_lose()
            print "Remaining counts:", count
    else  :
        print "Correct"
        new_game()

    
# create frame
frame=simplegui.create_frame("Guess_the_number", 200,200)
frame.add_input('your guess', input_guess,50)
frame.add_button('range 0-100', range100,100)
frame.add_button('range 0-1000', range1000,100)
# register event handlers for control elements and start frame

frame.start()
# call new_game 
new_game()



