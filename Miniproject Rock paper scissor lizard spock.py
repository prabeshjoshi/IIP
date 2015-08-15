

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name=="rock":
        number=0
    elif name=="Spock":
        number=1
    elif name== "paper":
        number= 2
    elif name== "lizard":
        number=3
    elif   name== "scissors":
        number=4
    else:
        print "enter valid name"
    return number    


def number_to_name(number) :
        if number==0:
            name="rock"
        elif number==1:
            name="Spock"
        elif number== 2:
            name= "paper"
        elif number==3 :
            name= "lizard"
        elif   number==4:
            name= "scissors"
        else:
            print "enter valid number"
        return name
    
  
import random

def rpsls(player_choice): 
    
    print
    player_number=name_to_number(player_choice)
    comp_number= random.randrange(0,5)
    comp_choice=number_to_name(comp_number)
   
    print "player chooses", player_choice
   
    print "Computer chooses", comp_choice 
    
    difference=comp_number-player_number
    if difference%5==0:
        result= "Tie"
    elif difference%5 == 1 or difference%5 == 2:
        result= "Computer wins!"
    else:
        result= "Player wins!"
    print result    
    
    

    

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




