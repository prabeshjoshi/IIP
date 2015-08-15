# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [300, 200]
vel = [-2,-2]
paddle1_pos= 200
paddle2_pos= 200
paddle1_vel = 0
paddle2_vel = 0
score_right= 0
score_left = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, vel # these are vectors stored as lists
    ball_pos = [300, 200]
    import random
    if direction == RIGHT:
        vel= [random.randrange(2, 5), -random.randrange(2, 5)]
        
    if direction == LEFT:
        vel= [-random.randrange(2, 5), -random.randrange(2, 5)]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel 
    global score_left, score_right
    spawn_ball(LEFT)
    score_right= 0
    score_left = 0
    button.set_text('Restart')

def draw(canvas):
    global score_left, score_right, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] +=  vel[0]       
    ball_pos[1] +=  vel[1]    
    # draw ball
    canvas.draw_circle(ball_pos ,BALL_RADIUS, 1, "White", 'white')
    if ball_pos[1]+BALL_RADIUS== HEIGHT or ball_pos[1]== BALL_RADIUS:
        vel[1]= -vel[1]
        
    elif ball_pos[0] <= 8 + BALL_RADIUS and (ball_pos[1] > paddle1_pos -HALF_PAD_HEIGHT) and (ball_pos[1]< paddle1_pos +HALF_PAD_HEIGHT):
            vel[0] = - 1.1*vel[0]
    elif ball_pos[0]+8+BALL_RADIUS >=600   and (ball_pos[1] > paddle2_pos -HALF_PAD_HEIGHT) and (ball_pos[1]< paddle2_pos +HALF_PAD_HEIGHT):
            vel[0] = - 1.1*vel[0]
       
    elif ball_pos[0] <= 8 + BALL_RADIUS:
        score_right += 1
        spawn_ball(RIGHT)
    elif ball_pos[0]+8+BALL_RADIUS >=600:
        score_left += 1
        spawn_ball(LEFT)
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos += paddle1_vel
    
    paddle2_pos += paddle2_vel
    if paddle1_pos >= 370:
        paddle1_pos = 362
    elif paddle1_pos <= 35:
        paddle1_pos = 43    
    if paddle2_pos >= 370:
        paddle2_pos = 362   
    elif paddle2_pos <= 35:
        paddle2_pos = 43        
       
    # draw paddles
    canvas.draw_line([4,paddle1_pos -HALF_PAD_HEIGHT], [4,paddle1_pos +HALF_PAD_HEIGHT], 8, 'blue')
    canvas.draw_line([596,paddle2_pos -HALF_PAD_HEIGHT], [596,paddle2_pos +HALF_PAD_HEIGHT], 8, 'green')
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score_right),[400,35], 35, "green")     
    canvas.draw_text(str(score_left),[200,35], 35, "blue")     
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 5
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 5    
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 5
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 5     
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel =0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0    
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0     



# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button=frame.add_button("New Game",new_game)



# start frame
new_game()
frame.start()
