# Module 5
#   Programming Assignment 6
#       Prob-1.py

# Matthew Bly

# INSTRUCTIONS:
#   Insert a comment above each line of code in the program below to describe
#   what the code does


from graphics import *

def main():
     # create the window
     win = GraphWin()

     # tells to draw the circle at point (50,50) with a radius of 20
     shape = Circle(Point(50,50), 20)

     # sets the outline color of the circle to red
     shape.setOutline("red")

     # fill the circle with the color red
     shape.setFill("red")

     # draws the cirlce
     shape.draw(win)
     
     for i in range(5):
          # creates a mouse icon
          p = win.getMouse()

          #returns a clone of the center point of the circle
          c = shape.getCenter()
          #gets the difference between the Original X Point and the new X point
          dx = p.getX() - c.getX()

          #gets the difference beteen the original Y point and the new Y point
          dy = p.getY() - c.getY()

          # moves the shape
          shape.move(dx,dy)

     # closes the window
     win.close()

main()