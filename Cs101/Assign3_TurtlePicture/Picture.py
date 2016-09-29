'''
Created on Feb 2, 2015

@author: Ivory
'''

import turtle
wn = turtle.Screen()
wn.setup(1000,600)
wn.bgcolor("lightblue")

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):    #This function helps create the circle by making a "polygon" with sides so small that it is a circle
        t.forward(sideLength)
        t.left(turnAngle)
    
def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius  #This function calls the polygon function and enters the parameters
    #calcs the circumference to know how big of a circle given the radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)
    
def grass():
    alex = turtle.Turtle()
    alex.color("darkgreen")
    alex.penup()
    alex.pensize(6)
    alex.left(180)
    alex.forward(500)    #SETS UP THE WINDOW SIZE AND MAKES THE GRASS :)
    alex.left(90)
    alex.forward(300)
    alex.left(90)     #FIGURE OUT HOW TO FILL THE GRASS
    alex.pendown()
    alex.left(45)
    alex.forward(50)
    
    for n in range(0,15):
        alex.right (90)
        alex.forward(50)
        alex.left(90)
        alex.forward(50)
    

def belly():
    bae = turtle.Turtle()
    bae.color("black","white")
    bae.penup()
    bae.pensize(7)
    bae.left(180)
    bae.forward(200)   #creates the belly and arms
    bae.left(90)
    bae.forward(150)
    bae.pendown()
    bae.begin_fill()
    drawCircle(bae,100)
    bae.begin_fill()
    bae.penup
    bae.right(180)
    bae.forward(25)
    bae.left(90)
    bae.forward(25)
    bae.pendown()
    bae.begin_fill()
    drawCircle(bae,25)
    bae.end_fill()
    bae.penup()
    bae.left(180)
    bae.forward(250)
    bae.right(90)
    bae.forward(50)
    bae.left(90)
    bae.pendown()
    bae.begin_fill()
    drawCircle(bae,25)
    bae.end_fill()
    
    
    
    
def foot1():
    billy = turtle.Turtle()
    billy.color("black","pink")
    billy.penup()
    billy.pensize(6)
    billy.left(180)
    billy.forward(195)   #creates foot one
    billy.left(90)
    billy.forward(215)
    billy.pendown()
    billy.begin_fill()
    drawCircle(billy,45)
    billy.end_fill()
def foot2():
    lina = turtle.Turtle()
    lina.color("black", "pink")
    lina.penup()
    lina.pensize(6)
    lina.left (180)
    lina.forward(87.5)   #creates foot two
    lina.left(90)
    lina.forward(215)
    lina.pendown()
    lina.begin_fill()
    drawCircle(lina,45)
    lina.end_fill()
    
def head():
    #draws the head
    sara = turtle.Turtle()
    sara.color("black","pink")
    sara.penup()
    sara.pensize(7)
    sara.left(180)    #creates head
    sara.forward(160)   
    sara.left(90)
    sara.pendown()
    sara.begin_fill()
    drawCircle(sara,60)
    sara.end_fill()

def eyes():
    lyn = turtle.Turtle()
    lyn.color("black","black")
    lyn.penup()
    lyn.pensize(7)
    lyn.left(180)
    lyn.forward(145)   
    lyn.left(180)
    lyn.forward(15)
    lyn.pendown()
    lyn.begin_fill()    #creates eyes
    drawCircle(lyn,10)
    lyn.end_fill()
    lyn.penup()
    lyn.forward(60)
    lyn.pendown()
    lyn.begin_fill()
    drawCircle(lyn,10)
    lyn.end_fill()
    

      

def draw(): #This function can only create turtles and call other functions
    grass()
    belly()
    foot1()
    foot2()
    head()
    eyes()
  

if __name__ == '__main__':
    # main function to have a turtle draw a picture 
    draw()
    
wn.exitonclick()   
        
    
    

    