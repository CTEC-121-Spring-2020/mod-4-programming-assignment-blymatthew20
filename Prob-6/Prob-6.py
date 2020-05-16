# Module 5
#   Programming Assignment 6
#       Prob-6.py

# Matthew Bly

from graphics import *

def main():
    win = GraphWin('Legos', 1100, 1000)

    #draw blue lego brick

    blueLegoBrick = Rectangle(Point(10, 200), Point(510, 100))
    blueLegoBrick.setFill('blue')
    blueLegoBrick.setOutline('black')
    blueLegoBrick.setWidth(5)
    blueLegoBrick.draw(win)

    blueBrickStub = Rectangle(Point(35, 100), Point(85, 80))
    blueBrickStub.setFill('blue')
    blueBrickStub.setOutline('black')
    blueBrickStub.setWidth(5)
    blueBrickStub.draw(win)

    for i in range(1, 5):
        blueBrickNextStub = blueBrickStub.clone()
        blueBrickNextStub.move(100 *i, 0)
        blueBrickNextStub.draw(win)

    #draw green lego brick
    greenLegoBrick = blueLegoBrick.clone()
    greenLegoBrick.setFill('green')
    greenLegoBrick.setOutline('black')
    greenLegoBrick.setWidth(5)
    greenLegoBrick.move(550,0)
    greenLegoBrick.draw(win)

    greenBrickStub = blueBrickStub.clone()
    greenBrickStub.setFill('green')
    greenBrickStub.setOutline('black')
    greenBrickStub.setWidth(5)
    greenBrickStub.move(550,0)
    greenBrickStub.draw(win)

    for i in range(1, 5):
        greenBrickNextStub = greenBrickStub.clone()
        greenBrickNextStub.move(100 *i, 0)
        greenBrickNextStub.draw(win)

    # draw yellow lego brick

    yellowLegoBrick = blueLegoBrick.clone()
    yellowLegoBrick.setFill('yellow')
    yellowLegoBrick.setOutline('black')
    yellowLegoBrick.setWidth(5)
    yellowLegoBrick.move(1,200)
    yellowLegoBrick.draw(win)

    yellowBrickStub = blueBrickStub.clone()
    yellowBrickStub.setFill('yellow')
    yellowBrickStub.setOutline('black')
    yellowBrickStub.setWidth(5)
    yellowBrickStub.move(.5,200)
    yellowBrickStub.draw(win)

    for i in range(1, 5):
        yellowBrickNextStub = yellowBrickStub.clone()
        yellowBrickNextStub.move(100 *i, 0)
        yellowBrickNextStub.draw(win)

    # draw red lego brick

    redLegoBrick = yellowLegoBrick.clone()
    redLegoBrick.setFill('red')
    redLegoBrick.setOutline('black')
    redLegoBrick.setWidth(5)
    redLegoBrick.move(550,0)
    redLegoBrick.draw(win)
    
    redBrickStub = greenBrickStub.clone()
    redBrickStub.setFill('red')
    redBrickStub.setOutline('black')
    redBrickStub.setWidth(5)
    redBrickStub.move(.5,200)
    redBrickStub.draw(win)

    for i in range(1,5):
        redBrickNextStub = redBrickStub.clone()
        redBrickNextStub.move(100 *i, 0)
        redBrickNextStub.draw(win)

    # draw cyan lego brick 

    cyanLegoBrick = yellowLegoBrick.clone()
    cyanLegoBrick.setFill('cyan')
    cyanLegoBrick.setOutline('black')
    cyanLegoBrick.setWidth(5)
    cyanLegoBrick.move(1,200)
    cyanLegoBrick.draw(win)

    cyanBrickStub = yellowBrickStub.clone()
    cyanBrickStub.setFill('cyan')
    cyanBrickStub.setOutline('black')
    cyanBrickStub.setWidth(5)
    cyanBrickStub.move(.5,200)
    cyanBrickStub.draw(win)

    for i in range(1, 5):
        cyanBrickNextStub = cyanBrickStub.clone()
        cyanBrickNextStub.move(100 *i, 0)
        cyanBrickNextStub.draw(win)

    # draw black lego brick

    blackLegoBrick = cyanLegoBrick.clone()
    blackLegoBrick.setFill('black')
    blackLegoBrick.setOutline('red')
    blackLegoBrick.setWidth(5)
    blackLegoBrick.move(550,0)
    blackLegoBrick.draw(win)

    blackBrickStub = redBrickStub.clone()
    blackBrickStub.setFill('black')
    blackBrickStub.setOutline('red')
    blackBrickStub.setWidth(5)
    blackBrickStub.move(.5,200)
    blackBrickStub.draw(win)

    for i in range(1,5):
        blackBrickNextStub = blackBrickStub.clone()
        blackBrickNextStub.move(100 *i, 0)
        blackBrickNextStub.draw(win)

    win.getMouse()     
    win.close()


    


main()