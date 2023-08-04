

student_number = 11066440 
student_name   = 'Mohamad Dabboussi' #
 



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You must NOT change
# any of the code in this section.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile
from entity_data import entity_actions
import time

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless
# instructed.
cell_size = 100 # pixels (default is 100)
grid_width = 8 # squares (default is 8)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.5 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 5, 'normal') # font for the coords
big_font = ('Arial', cell_size // 4, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 7, 'Grid must be at least 7 squares wide'
assert (grid_height >= 5) and (grid_height % 2 != 0), \
       'Grid must be at least 5 squares high and height must be odd'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True,
                          label_spaces = True): # NO! DON'T CHANGE THIS!
    
    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(str(x_label + 1), align = 'right', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 5, cell_size // 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(chr(y_label + ord('A')), align = 'center', font = small_font)

        # Mark the two "special" cells
        goto(-cell_size * grid_width // 2 + 0.5 * cell_size, 0)
        dot(cell_size // 6)
        goto(cell_size * grid_width // 2 - 0.5 * cell_size, 0)
        dot(cell_size // 6)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1.15) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ntwo states of\nyour first\nentity here', align = 'right', font = big_font)    
        # Right side
        goto(((grid_width + 1.15) * cell_size) // 2, -(cell_size // 2))
        write('Draw the\ntwo states of\nyour second\nentity here', align = 'left', font = big_font)    

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = False):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "track_entities" function.  ALL of your solution code
#  must appear in, or be called from, function "track_entities".  Do
#  NOT put any of your code in other parts of the program and do NOT
#  change any of the provided code except as allowed in the main
#  program below.
#

# All of your code goes in, or is called from, this function



def track_entities(actions):
    
    
    def Sad_Patrick(x=0,y=0):
    #Sad Patrick's Background
        home()
        fillcolor('orange')
        goto((-cell_size*5.5)+x,(-cell_size)+y)
        if (xcor()<-400 or xcor()>400 or ycor()<-350 or ycor()>350):
            if (x==0 and y==0):
                pass
            else:
                return False
            
        left(135)
        forward(sin(radians(45))*cell_size)
        setheading(0)
        pendown()
        begin_fill()
        for square in range(4):
            forward(100)
            right(90)
        end_fill()
        penup()
    # Drawing Sad Patrick's Body
        goto(-590+x,-150+y)
        left(60)
        pencolor('red')
        fillcolor('#f88379')
        pensize(1)
        pendown()
        begin_fill()
        forward(30)
        left(15)
        forward(60)
        circle(-8,extent=150)
        forward(60)
        left(15)
        forward(30)
        end_fill()
        penup()
     #Drawing Sad Patrick's Eyes
        goto(-555+x,-100+y)
        setheading(45)
        pendown()
        pencolor('black')
        fillcolor('white')
        pensize(1)
        begin_fill()
        for right_eye_shape in range(2):
            circle(11,extent=90)
            circle(3,extent=90)
       
        penup()
        goto(-545+x,-100+y)
        setheading(45)
        pendown()
        for left_eye_shape  in range(2):
            circle(11,extent=90)
            circle(3,extent=90)
        end_fill()
        penup()
        setheading(90)
        forward(6)
        left(90)
        forward(3)
    #Patrick's left pupil
        dot(5,'black')
        penup()
        forward(9)
        pendown()
     #patrick's right pupil
        dot(5,'black')
        penup()
     #Making his eyes tired
        forward(5)
        setheading(0)
        pendown()
        pencolor('Black')
        fillcolor('blue')
        begin_fill()
        forward(10)
        setheading(90)
        circle(11,45)
        circle(3.5,90)
        circle(11,45)
        end_fill()
        setheading(0)
        forward(10)
        fillcolor('blue')
        begin_fill()
        forward(12)
        setheading(90)
        circle(11,45)
        circle(3.5,90)
        circle(11,45)
        end_fill()
        penup()
     #Patrick's Frown
        goto(-560+x,-112+y)
        setheading(15)
        pensize(1)
        pendown()
        for mouth in range(10):
            left(1)
            forward(1)
        
        setheading(5)
        for mouth in range(10):
            right(1)
            forward(1)
        penup()
     #Patrick's eyebrows
        goto(-558+x,-80+y)
        setheading(45)
        pensize(3)
        pendown()
        forward(6)
        penup()
        setheading(0)
        forward(4)
        right(45)
        pendown()
        forward(6)
        penup()
    #Patrick's Pants
        goto(-582+x,-150+y)
        setheading(60)
        pencolor('black')
        fillcolor('chartreuse')
        pensize(1)
        pendown()
        begin_fill()
        forward(15)
        setheading(0)
        forward(45)
        right(60)
        forward(15)
        end_fill()
        penup()
     #Designing Patrick's pants
        go_to=[(-555+x,-142+y),(-533+x,-145+y)]
        for loop in range(len(go_to)):
          goto(go_to[loop])
          pencolor('purple')
          setheading(180)
          pendown()
          dot(7,'purple')
          forward(5)
          dot(10,'purple')
          forward(5)
          dot(7,'purple')
          penup()
        
        
     #patricks Broken Hearts
        go_to1=[(-530+x,-75+y),(-588+x,-93+y),(-520+x,-110+y)]
        for loop in range(len(go_to1)):
          goto(go_to1[loop])
          setheading(135)
          pencolor('black')
          fillcolor('red')
          pensize(1)
          pendown()
          begin_fill()
          forward(9)
          for curve in range(20):
              right(10)
              forward(1)
          setheading(45)
          for curve in range(20):
              right(10)
              forward(1)
          forward(10)
          end_fill()
          penup()
          setheading(50)
          pendown()
          forward(7)
          left(90)
          forward(7)
          right(90)
          forward(7)
          penup()
          return True
    
          
    def Happy_Patrick(x=0,y=0):

     #Happy Patrick's Background
        goto((-cell_size*5.5)+x,cell_size+y)
        if (xcor()<-400 or xcor()>400 or ycor()<-350 or ycor()>350):
            if (x==0 and y==0):
                pass
            else:
                return False
        if xcor()>0 and actions[0][1]=='Unwell':
            if (x==0 and y==0):
                pass
            else:
                print("*",x,y)
                actions[0][0]='Unwell'
                return Sad_Patrick(x,y+200)
        fillcolor('Yellow')
        setheading(135)
        forward(sin(radians(45))*cell_size)
        setheading(0)
        pendown()
        begin_fill()
        for square in range(4):
            forward(100)
            right(90)
        end_fill()
        penup()
    #Happy Patrick's Body
        goto(-575+x,78+y)
        setheading(95)
        fillcolor('#f88379')
        pencolor('red')
        begin_fill()
        pendown()
        forward(6)
        for curve in range(6):
            right(9)
            forward(1)
        setheading(60)
        begin_fill()
        forward(20)
     #drawing Patrick's right arm
        left(90)
        forward(20)
        for right_hand in range(10):
            forward(1)
            left(20)
        right(40)
        forward(22)
        setheading(60)
        forward(20)
    #Drawing Patrick's Face
        setheading(75)
        forward(20)
        for head in range(10):
            right(5)
            forward(2)
        setheading(310)
        for head in range(12):
            right(5)
            forward(1)
        setheading(280)
        forward(28)
    #drawing Patricks's left arm
        right(75)
        forward(4)
        right(180)
        forward(24)
        for left_hand in range(10):
            forward(1)
            right(20)
        setheading(225)
        forward (30)
        right(180)
        forward(9)
        setheading(290)
        for lower_body_curve in range(9):
            forward(2)
            right(6)
        setheading(210)
        pencolor('black')
        for belly in range(26):
          forward(1.95)
          right(2.7) 
        end_fill()
     #Patrick's Pants
        right(180)
        fillcolor('chartreuse')
        pencolor('chartreuse')
        begin_fill()
        for belly in range(26):
          forward(1.95)
          left(2.85) 
        setheading(255)
        pencolor('black')
        for back_curve in range(9):
            forward(2)
            right(6)
        setheading(270)
        forward(4)
        right(90)
        forward(8)
        right(90)
        forward(4)
        setheading(180)
        for curve in range(17):
            forward(2.05)
            right(4.25)
        end_fill()
        penup()
        go_to4=[(-555+x,69+y),(-540+x,67+y)]
        for loop in range(len(go_to4)):#Pant's design
          goto(go_to4[loop])
          pencolor('purple')
          setheading(180)
          pendown()
          dot(4,'purple')
          forward(3)
          dot(5,'purple')
          forward(3)
          dot(4,'purple')
          penup()
     #patrick's left foot
        goto(-548+x,60+y)
        pencolor('red')
        fillcolor('#f88379')
        pendown()
        begin_fill()
        setheading(270)
        circle(3,180)
        setheading(180)
        pencolor('black')
        forward(6)
        end_fill()
        penup()
     #patrick's right foot
        goto(-560+x,60+y)
        pencolor('red')
        fillcolor('#f88379')
        pendown()
        begin_fill()
        setheading(270)
        circle(3,180)
        setheading(180)
        forward(6)
        end_fill()
        fillcolor('chartreuse')
        pencolor('black')
        begin_fill()
        setheading(90)
        forward(6.2)
        right(180)
        forward(6.2)
        setheading(0)
        forward(6)
        left(90)
        forward(5)
        left(90)
        pencolor('black')
        forward(6)
        end_fill()
        penup()
    #Patrick's eyes
        goto(-553+x,114+y)
        setheading(45)
        pendown()
        pencolor('black')
        fillcolor('white')
        pensize(1)
        begin_fill()
        for right_eye_shape in range(2):
            circle(9,extent=90)
            circle(2,extent=90)
        end_fill()
        penup()
        goto(-547+x,114+y)
        setheading(45)
        pendown()
        pencolor('black')
        fillcolor('white')
        begin_fill()
        for left_eye_shape  in range(2):
            circle(9,extent=90)
            circle(2,extent=90)
        end_fill()
        go_to2=[(-555+x,120+y),(-549+x,120+y)]
        for loop in range(len(go_to2)):
            penup()
            goto(go_to2[loop])
            pendown()
            dot(4,'black')
        penup()
     #Patrick's eyebrows
        goto(-552+x,134+y)
        setheading(225)
        pencolor('black')
        pensize(2)
        pendown()
        forward(4)
        penup()
        goto(-549+x,134+y)
        setheading(315)
        pendown()
        forward(4)
        penup()
     #Patrick's Mouth(Smile)
        goto(-558+x,105+y)
        fillcolor('crimson')
        setheading(349)
        pensize(1)
        pendown()
        begin_fill()
        circle(20,40)
        penup()
        setheading(260)
        pendown()
        for smile in range(23):
            forward(1)
            right(5)
        penup()
        right(175)
        forward(2)
        setheading(45)
        pendown()
        circle(20,25)
        end_fill()
        penup()
        return True
    
      
    def Happy_Spongebob(x=0,y=0):
     #Happy Spongebob Background
        goto((cell_size*5.5)+x,cell_size+y)
        print("s",xcor(),ycor())
        if (xcor()<-400 or xcor()>400 or ycor()<-350 or ycor()>350):
            if (x==0 and y==0):
                pass
            else:
                return False
        if xcor()<0 and actions[0][0]=='Unwell':
            print("*",x,y)
            actions[0][1]='Unwell'
            return Sick_Spongebob(x,y+200)
        else:
            pass
        fillcolor('light Blue')
        setheading(135)
        forward(sin(radians(45))*cell_size)
        setheading(0)
        pendown()
        begin_fill()
        for square in range(4):
            forward(100)
            right(90)
        end_fill()
        penup()
    #spongebob's head
        goto(515+x,145+y)
        fillcolor('yellow')
        pencolor('black')
        begin_fill()
        pendown()
        setheading(330)
        for head in range(6):
            circle(6,60)
            circle(-6,60)
        setheading(235)
        for head in range (5):
            circle(7,60)
            circle(-7,60)
        setheading(180)
        forward(62)
        setheading(65)
        for head in range(5):
            circle(7,60)
            circle(-7,60)
        end_fill()
        penup()
    #Spongebob's eyes
        fillcolor('white')
        begin_fill()
        goto(552+x,120+y)
        pendown()
        setheading(90)
        circle(10)
        end_fill()
        begin_fill()
        goto(550+x,120+y)
        pendown()
        setheading(90)
        circle(-10)
        end_fill()
        penup()
    #spongebob left eye pupil
        goto(554+x,120+y)
        fillcolor('blue')
        pendown()
        setheading(90)
        begin_fill()
        circle(-4)
        end_fill()
        penup()
        setheading(0)
        forward(4)
        dot(4,'black')
    #Spongebob right eye pupil
        goto(547+x,120+y)
        fillcolor('blue')
        pendown()
        setheading(90)
        begin_fill()
        circle(4)
        end_fill()
        penup()
        setheading(180)
        forward(4)
        dot(4,'black')
        penup()
    #Sponebob nose
        goto(548+x,110+y)
        setheading(115)
        fillcolor('yellow')
        begin_fill()
        pendown()
        forward(6)
        setheading(0)
        forward(8)
        setheading(245)
        forward(6)
        end_fill()
        penup()
    #spongebob smile
        goto(530+x,100+y)
        setheading(305)
        pendown()
        circle(15,50)
        setheading(0)
        forward(20)
        circle(15,55)
        penup()
    #spongebob teeth
        goto(530+x,100+y)
        setheading(305)
        circle(15,50)
        setheading(0)
        forward(4)
        fillcolor('white')
        begin_fill()
        right(90)
        pendown()
        forward(6)
        left(90)
        forward(6)
        left(90)
        forward(6)
        left(90)
        forward(6)
        end_fill()
        penup()
        right(180)
        forward(8)
        begin_fill()
        right(90)
        pendown()
        forward(6)
        left(90)
        forward(6)
        left(90)
        forward(6)
        left(90)
        forward(6)
        end_fill()
        penup()
    #Spongebob Cloth
        goto(519+x,74+y)
        fillcolor('white')
        begin_fill()
        setheading(280)
        pendown()
        forward(12)
        setheading(0)
        forward(58)
        setheading(80)
        forward(12)
        end_fill()
        penup()
        right(180)
        fillcolor('brown')
        forward(12)
        pendown()
        begin_fill()
        forward(12)
        setheading(180)
        penup()
        forward(54)
        setheading(100)
        pendown()
        forward(12)
        end_fill()
    #Drawing Sleeves
        fillcolor('white')
        begin_fill()
        setheading(180)
        forward(10)
        setheading(58)
        forward(15)
        end_fill()
        setheading(280)
        pendown()
        forward(12)
        setheading(0)
        forward(58)
        setheading(80)
        forward(12)
        begin_fill()
        setheading(303)
        forward(15)
        setheading(180)
        forward(10)
        end_fill()
        setheading(80)
        forward(12)
        penup()
        #Spongebob's Arms
        setheading(303)
        forward(15)
        setheading(180)
        forward(2)
        fillcolor('yellow')
        pencolor('black')
        pendown()
        begin_fill()
        setheading(270)
        forward(12)
        right(90)
        forward(5)
        right(90)
        forward(12)
        right(90)
        forward(5)
        end_fill()
        right(180)
        forward(68)
        begin_fill()
        setheading(270)
        forward(12)
        right(90)
        forward(5)
        right(90)
        forward(12)
        right(90)
        forward(5)
        end_fill(),x,y
        penup()
    #Spongebob's red tie
        goto(545+x,74+y)
        fillcolor('red')
        setheading(310)
        begin_fill()
        pendown()
        forward(8)
        setheading(0)
        forward(6)
        setheading(55)
        forward(9)
        setheading(180)
        forward(7)
        end_fill()
        penup()
        goto(545+x,74+y)
        setheading(310)
        forward(8)
        fillcolor('red')
        setheading(260)
        begin_fill()
        pendown()
        forward(10)
        left(50)
        forward(6)
        left(90)
        forward(8)
        left(70)
        forward(10)
        setheading(180)
        forward(6)
        end_fill()
        penup()
        return True
    

    def Sick_Spongebob(x=0,y=0):

    #Affected spongebob Background
        goto((cell_size*5.5)+x,-cell_size+y)
        if (xcor()<-400 or xcor()>400 or ycor()<-350 or ycor()>350):
            if (x==0 and y==0):
                pass
            else:
                return False
        fillcolor('light green')
        setheading(135)
        forward(sin(radians(45))*cell_size)
        setheading(0)
        pendown()
        begin_fill()
        for square in range(4):
            forward(100)
            right(90)
        end_fill()
        penup()
        #head
        goto(508+x,-60+y)
        fillcolor('yellow')
        pencolor('black')
        begin_fill()
        pendown()
        setheading(325)
        for head in range(6):
            circle(6,60)
            circle(-6,60)
        setheading(230)
        for head in range (5):
            circle(7,60)
            circle(-7,60)
        setheading(175)
        forward(62)
        setheading(60)
        for head in range(5):
            circle(7,60)
            circle(-7,60)
        end_fill()
        penup()
        goto(508+x,-60+y)
        pencolor('black')
        setheading(325)
        for head in range(6):
            circle(6,60)
            circle(-6,60)
        setheading(300)
        begin_fill()
        pendown()
        for head in range(1):
            circle(6,60)
            circle(-6,60)
        setheading(230)
        for head in range (5):
            circle(7,60)
            circle(-7,60)
        setheading(144)
        forward(12)
        end_fill()
    #White Blanket
        setheading(175)
        fillcolor('white')
        forward(68)
        right(180)
        begin_fill()
        forward(100)
        setheading(270)
        forward(15)
        setheading(180)
        forward(100)
        end_fill()
        penup()
    #Spongebob's mask
        goto(515+x,-100+y)
        pencolor('grey')
        begin_fill()
        setheading(355)
        pendown()
        forward(45)
        right(95)
        forward(15)
        right(63)
        for mask in range(22):
          forward(2)
          right(2)
        setheading(85)
        forward(16)
        end_fill()
        setheading(170)
        forward(10)
        penup()
        goto(515+x,-100+y)
        setheading(355)
        pendown()
        forward(58)
        left(15)
        forward(12)
        penup()
        goto(515+x,-100+y)
        setheading(355)
        forward(45)
        right(95)
        forward(15)
        setheading(355)
        pendown()
        forward(12)
        left(15)
        forward(12)
        penup()
        goto(515+x,-100+y)
        setheading(275)
        forward(16)
        setheading(175)
        pendown()
        forward(10)
        penup()
        #Spongebob's eyes
        goto(540+x,-85+y)
        setheading(85)
        pencolor('black')
        pendown()
        circle(8)
        penup()
        goto(537+x,-85+y)
        fillcolor('yellow')
        begin_fill()
        pendown()
        circle(-8)
        end_fill()
        setheading(355)
        forward(12)
        right(180)
        penup()
        forward(26)
        right(180)
        pendown()
        forward(12)
        penup()
        #Spongebob's nose under mask
        goto(537+x,-98+y)
        setheading(250)
        pendown()
        forward(4)
        penup()
        return True
     

    Sick_Spongebob()
    Happy_Spongebob()
    Happy_Patrick()
    Sad_Patrick()
    penup()
    #titles
    pencolor('black')
    goto(-450,25)
    pendown()
    write('"LET US GO JELLYFISHING"',align='right',font=('Arial',10))
    penup()
    goto(-480,-175)
    pendown()
    write('" Being Heartbroken Hurts "',align='right',font=('Arial',10))
    penup()
    goto(-520,200)
    pendown()
    write('Patrick',align='right',font=('Arial',14))
    penup()
    goto(500,200)
    pendown()
    write('Spongebob',align='left',font=('Arial',14))
    penup()
    goto(500,25)
    pendown()
    write('"Aye Aye Captain"',align='left',font=('Arial',10))
    penup()
    goto(500,-175)
    pendown()
    write('"Not So Anti-Covid"',align='left',font=('Arial',10))
    penup()

    x_patrick_new = 0
    y_patrick_new = 0
    x_sponge_new = 0
    y_sponge_new = 0
    x_patrick_old = 0
    y_patrick_old = 0
    x_sponge_old = 0
    y_sponge_old = 0
    
#determine which Image do we need 
    def which_patrick_image(x1=0,y1=0):#function for selected patrick image
        if actions[0][0]== 'Healthy':
            x=((+cell_size*5.5)-(cell_size*3.5))+x1
            y= -cell_size+y1
            if not Happy_Patrick(x,y):
                return False
        else:#unwell
            x=((+cell_size*5.5)-(cell_size*3.5))+x1
            y=+ cell_size+y1
            if not Sad_Patrick(x,y):
                return False
        return True
    which_patrick_image()
    def which_spongebob_image(x2=0,y2=0):#function for the selected spongebob image
        if actions[0][1]=='Healthy':
            x=-((+cell_size*5.5)-(cell_size*3.5))+x2
            y= -cell_size+y2
            if not Happy_Spongebob(x,y):
                return False
        else:#unwell
            x=-((+cell_size*5.5)-(cell_size*3.5))+x2
            y=+ cell_size+y2
            if not Sick_Spongebob(x,y):
                return False
        return True
    which_spongebob_image()
    for pair in actions[1:]:#take out the parts of actions
        image=pair[0]#it tells whether patrick's or Spongebob's image will move
        command=pair[1]#the direction it will move in
        how_much=pair[2]#by how many cells is it moving
        if image=='Left entity':
                for loop in range (how_much):
                    if command=='North':#going up
                        x_patrick_new = x_patrick_old
                        y_patrick_new = y_patrick_old + cell_size
                    elif command== 'South':#going down
                        x_patrick_new = x_patrick_old
                        y_patrick_new = y_patrick_old - cell_size
                    elif command== 'East':#going right
                        x_patrick_new = x_patrick_old + cell_size
                        y_patrick_new = y_patrick_old
                    elif command== 'West':#going left
                        x_patrick_new = x_patrick_old - cell_size
                        y_patrick_new = y_patrick_old
                    if which_patrick_image(x_patrick_new,y_patrick_new):
                        x_patrick_old = x_patrick_new
                        y_patrick_old = y_patrick_new

        elif image=='Right entity':
                for loop in range (how_much):
                    if command=='North':#going up
                        x_sponge_new = x_sponge_old
                        y_sponge_new = y_sponge_old + cell_size
                    elif command== 'South':#going down
                        x_sponge_new = x_sponge_old
                        y_sponge_new = y_sponge_old - cell_size
                    elif command== 'East':#going right
                        x_sponge_new = x_sponge_old + cell_size
                        y_sponge_new = y_sponge_old
                    elif command== 'West':#going left
                        x_sponge_new = x_sponge_old - cell_size
                        y_sponge_new = y_sponge_old
                    if which_spongebob_image(x_sponge_new,y_sponge_new):
                        x_sponge_old = x_sponge_new
                        y_sponge_old = y_sponge_new
    hideturtle()
                    

                        

            
                
            

    

    
    
    
    
    
    
        
    
    
    
    
        
    
    
    
    
    



               
    
    
    
    
        
        
    
        
    
    
    

#
#--------------------------------------------------------------------#



#-----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  You
# should NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's data generation function if available, but
### otherwise creating a dummy function that returns an empty
### list
if isfile('entity_data.py'):
    print('\nData module found\n')
    from entity_data import entity_actions
    def actions(new_seed = None):
        seed(new_seed)
        return entity_actions(grid_width, grid_height)
else:
    print('\nNo data module available!\n')
    def actions(dummy_parameter = None):
        return []

#
#--------------------------------------------------------------------#



#-----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call

create_drawing_canvas(label_spaces=False)

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
title("Spongebob And Patrick")

# Call the student's function to process the data set
# ***** While developing your program you can call the
# ***** "actions" function with a fixed seed for the
# ***** random number generator, but your final solution must
# ***** work with "actions()" as the argument to "track_entities",
# ***** i.e., for any data set that can be returned by
# ***** calling function "actions" with no seed.
track_entities(actions()) # <-- no argument for "actions" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible when the program
# ***** terminates as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
