# Module 5
#   Programming Assignment 6
#       Prob-5.py

# Matthew Bly

from graphics import *

def main():
    win = GraphWin("Matthews Car",800, 800)
    
     #car Frame
    p1 = Point(600,320)
    p2 = Point(150,400)
    CarFrame = Rectangle(p1 , p2)
    CarFrame.setOutline("red")
    CarFrame.setFill("red")
    CarFrame.draw(win)

    #back wheel 
    BackWheel = Circle(Point(550, 410), 50)
    BackWheel.setOutline("black")
    BackWheel.setFill("black")
    BackWheel.draw(win)
    
    #back wheel inner cirlce
    BackWheel = Circle(Point(550, 410), 25)
    BackWheel.setOutline("gray")
    BackWheel.setFill("gray")
    BackWheel.draw(win)

    #front wheel
    FrontWheel = Circle(Point(200, 410), 50)
    FrontWheel.setOutline("black")
    FrontWheel.setFill("black")
    FrontWheel.draw(win)

    #front wheel inner circle
    FrontWheel = Circle(Point(200, 410), 25)
    FrontWheel.setOutline("gray")
    FrontWheel.setFill("gray")
    FrontWheel.draw(win)
   
    #back Bumper
    p1 = Point(130,350)
    p2 = Point(150,400)
    BackBumper = Rectangle(p1 , p2)
    BackBumper.setOutline("gray")
    BackBumper.setFill("blue")
    BackBumper.draw(win)

    #Front Bumper
    p1 = Point(610,350)
    p2 = Point(600,400)
    FrontBumper = Rectangle(p1 , p2)
    FrontBumper.setOutline("gray")
    FrontBumper.setFill("green")
    FrontBumper.draw(win)

    # Car Polygon
    CarPolygon = Polygon(Point(160,250), Point(160,319), Point(220,320))
    CarPolygon.setOutline("black")
    CarPolygon.setFill("black")
    CarPolygon.draw(win)

    # Car Roof and windows
    aLine = Line(Point(320,250), Point(480,250))
    aLine.setOutline('blue')
    aLine.setFill("blue")
    aLine.draw(win)

    bLine = Line(Point(320,250), Point(250, 320))
    bLine.setOutline('blue')
    bLine.setFill("blue")
    bLine.draw(win)

    cLine = Line(Point(380,250), Point(380, 320))
    cLine.setOutline('blue')
    cLine.setFill("blue")
    cLine.draw(win)
    
    dLine = Line(Point(480,250), Point(530, 320))
    dLine.setOutline('blue')
    dLine.setFill("blue")
    dLine.draw(win)
    
    

    win.getMouse()     
    win.close()
main()