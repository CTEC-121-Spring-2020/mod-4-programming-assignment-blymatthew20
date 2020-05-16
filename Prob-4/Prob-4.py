# Module 5
#   Programming Assignment 6
#       Prob-4.py

# Matthew Bly

from graphics import *

def main():
    
    win = GraphWin('Matthew Bly House',800, 800)
    
    # draw the house frame
    p1 = win.getMouse()
    p2 = win.getMouse()
    frame = Rectangle(p1, p2)
    frame.draw(win)
    houseBottomY = min(p1.getY(), p2.getY())
    houseTopY = max(p1.getY(), p2.getY())
    houseLeftX = min(p1.getX(), p2.getX())
    houseRighX = max(p1.getX(), p2.getX())

    # draw the door
    p3 = win.getMouse()
    doorW = abs(p1.getX() - p2.getX()) * 0.2
    doorH = abs(p3.getY() - houseBottomY)
    doorP1 = Point(p3.getX() - doorW * 0.5, houseBottomY)
    doorP2 = Point(p3.getX() + doorW * 0.5, p3.getY())
    door = Rectangle(doorP1, doorP2)
    door.draw(win)
   
    # draw the window
    p4 = win.getMouse()
    windowH = doorW * 0.5
    windowP1 = Point(p4.getX() - windowH * 0.5, p4.getY() - windowH * 0.5)
    windowP2 = Point(p4.getX() + windowH * 0.5, p4.getY() + windowH * 0.5)
    window = Rectangle(windowP1, windowP2)
    window.draw(win)

    # Draw the roof
    p5 = win.getMouse()
    roofP1 = Point(houseLeftX, houseTopY)
    roofP2 = Point(houseRighX, houseTopY)
    roofP3 = p5
    roof = Polygon(roofP1, roofP2, roofP3)
    roof.draw(win)
    win.getMouse()
    win.close


main()