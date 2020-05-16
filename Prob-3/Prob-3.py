# Module 5
#   Programming Assignment 6
#       Prob-3.py

# Matthew Bly

from graphics import *

def main():
    win = GraphWin('Archery Target',800,800)
    center = Point(400,400)
 
    whiteCircle = Circle(center, 100)
    whiteCircle.setFill('white')
    whiteCircle.draw(win)
 
    blackCirlce = Circle(center, 80)
    blackCirlce.setFill('black')
    blackCirlce.draw(win)
 
    blueCircle = Circle(center, 60)
    blueCircle.setFill('blue')
    blueCircle.draw(win)
 
    redCircle = Circle(center, 40)
    redCircle.setFill('red')
    redCircle.draw(win)
 
    yellowCircle = Circle(center, 20)
    yellowCircle.setFill('yellow')
    yellowCircle.draw(win)
 
    win.getMouse() 
    win.close()

main()    