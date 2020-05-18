# Module 5
#   Programming Assignment 6
#       Prob-2.py

# Matthew Bly

from graphics import *

def main():
     # creates window
     
     win = GraphWin("Problem 2",400, 400)

     #draws square
     p1 = Point(50,50)
     p2 = Point(100,100)
     shape = Rectangle(p1, p2)
     shape.setOutline("red")
     shape.setFill("red")
     shape.draw(win)

     #draws squares without moving orignal
     for i in range(5):
          p = win.getMouse()
          shape = Rectangle(p, Point(p.getX()+50, p.getY()+50))
          shape.setOutline("red")
          shape.setFill("red")
          shape.draw(win)

     #displays text to click the screen again to quit
     Text(Point(200,200),"Click again to quit").draw(win)
     win.getMouse()     
     win.close()
     


main()