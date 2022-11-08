#This is a little program written in a programming language called
#Python
#The goal of this game is for Dylan the turtle to escape Daddy's maze!

#This will get some things we need for the game to work
#an import gets a library into your program
import turtle

daddy = turtle.Turtle()
dylan = turtle.Turtle()

dylan.shape('turtle')

#  The first block of code lifts the pen and moves it to the (x,y) coordinates (100,200) then puts the pen down again. (By default, the pens will draw as they move so this moves to a new starting location without making a line.)
daddy.up()

daddy.setx(100)
daddy.sety(200)
daddy.down()

# The next line changes the color to any color I choose
daddy.color('cyan')

#This first line draws the first line of the maze
daddy.right(90)
daddy.forward(300)
daddy.up()

#Move dylan down
dylan.down()
dylan.right(90)
dylan.forward(110)
dylan.left(90)
dylan.forward(120)