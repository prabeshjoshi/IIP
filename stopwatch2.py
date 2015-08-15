#Stopwatch game
import simplegui 
millisecs= 0     # initiallizing values
mil=0
wins=0
tries=0
scored_once = True  # boolean to check if wins & tries have been updated before
text="Get points by stopping the timer at one whole second"
message =" "

#converts the number of tick (here: millisecs) to a format ..MM:SS:C 
def convert(millisecs):
    global mil
    mil=millisecs%10
    seconds= millisecs//10
    minutes=millisecs//600
    sec=seconds%60   
    sec2=sec%10   #2nd digit of seconds
    sec1=sec//10	   #1st digit of seconds
    min2=minutes%10  #2nd digit of minutes
    min1=minutes//10
    return str(min1)+str(min2)+":"+str(sec1)+str(sec2)+"."+str(mil)

def stop():
    timer.stop()
    global wins
    global tries
    global scored_once
    global message
    
    if scored_once== False:   # if not scored already, run this! else do nothing
        if mil==0:
            wins+=1  
            tries+=1
            scored_once=True 
            message = "Bingo!"
        else:
            tries+=1
            scored_once=True
            message = "Nice Try"
            
                   
def  tick():
    global millisecs
    millisecs += 1 
    
def start():
    global scored_once
    global message
    scored_once= False
    timer.start()
    message= " "
    

def reset():
    global millisecs 
    global wins, tries, scored_once, message
    scored_once = True
    millisecs =0
    timer.stop()
    message= " "
    wins=0
    tries =0
    
# Handler to draw on canvas
def draw(canvas):
       canvas.draw_text(convert(millisecs), [50,112], 48, "Red")
       canvas.draw_text( str(wins)+"/"+str(tries), [250,40], 25, "green")   
       canvas.draw_text( message, [2,40], 25, "green")   
    

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Beat the Timer!!", 300, 200)
frame.add_button("stop", stop, 150)
frame.add_button("start", start, 150)
frame.add_button("reset", reset, 150)
frame.add_label(text)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# Start the frame animation
frame.start()
