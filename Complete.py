# implementation of card game - Memory

import simplegui
import random
state = 0
firt_card, second_card, turns = 0,0,0
image = simplegui.load_image("http://images4.fanpop.com/image/forum/82000/82216_1293997973710_full.jpg")

 
# helper function to initialize globals
def new_game():
    global lis, exposed, turns
    lis = range(0,8)*2
    import random
    random.shuffle(lis)
    exposed = [False]*16
    state = 0
    turns = 0
    label.set_text("Turns = "+str(turns))
    
    
     
# define event handlers
def mouseclick(pos):
    global exposed, first_card, second_card, turns
    # add game state logic here
    
    
    global state
    if exposed[pos[0]//50] == False:
        
        label.set_text("Turns = "+str(turns))
                       
        if state == 0:
             
            exposed[int(pos[0]//50)] = True
            first_card = int(pos[0]//50)
               
            state = 1
        
        elif state == 1:
            exposed[int(pos[0]//50)] = True
            turns += 1
            if lis[pos[0]//50] == lis[first_card]:
                state = 0
            else:
            
                second_card = int(pos[0]/50)
                state = 2    
            
        else:
            exposed[int(pos[0]//50)] = True
            exposed[first_card] = False
            
            if lis[pos[0]//50] == lis[second_card] :
                state = 0
            
            else:
                exposed[int(second_card)] = False
                first_card = pos[0]//50
                state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global lis, exposed
    c= 25
    for num in range(len(lis)):
        if exposed[num] == True: 
            canvas.draw_text(str(lis[num]), [c, 50], 30, 'Red')
        else:
            canvas.draw_line((c, 0), (c, 100), 49, 'green')
        c += 50
    
    

    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label=frame.add_label('Turns = 0')


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric