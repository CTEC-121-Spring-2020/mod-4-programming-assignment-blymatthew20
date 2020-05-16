# Module 5
#   Programming Assignment 6
#       Prob-7.py

# Matthew Bly

from graphics import *

def main():
        win = GraphWin('Face',800,800)
        center = Point(400,400)

        #draw face outline
        face = Circle(center,200)
        face.setOutline('black')
        face.setFill('pink')
        face.draw(win)

        #left eye
        leftEye = Circle(center,50)
        leftEye.setOutline('black')
        leftEye.setFill('white')
        leftEye.move(-100,-100)
        leftEye.draw(win)
        leftEye = Circle(center,25)
        leftEye.setFill('brown')
        leftEye.setOutline('black')
        leftEye.move(-100,-100)
        leftEye.draw(win)

        #right eye
        rightEye = Circle(center,50)
        rightEye.setOutline('black')
        rightEye.setFill('white')
        rightEye.move(100,-100)
        rightEye.draw(win)
        rightEye = Circle(center,25)
        rightEye.setFill('brown')
        rightEye.setOutline('black')
        rightEye.move(100,-100)
        rightEye.draw(win)

        #nose
        nose = Polygon(Point(400,350), Point(300,400), Point(500,400))
        nose.setFill('black')
        nose.setOutline('black')
        nose.draw(win)

        #mouth
        mouth = Oval(Point(580,430), Point(220,520))
        mouth.setOutline('black')
        mouth.setFill('red')
        mouth.draw(win)

        #teeth
        toothOne = Rectangle (Point(400,520), Point(380,470))
        toothOne.setFill('white')
        toothOne.setOutline('black')
        toothOne.draw(win)
        
        toothTwo = toothOne.clone()
        toothTwo.setFill('white')
        toothTwo.setOutline('black')
        toothTwo.move(42,0)
        toothTwo.draw(win)

        toothThree = toothOne.clone()
        toothThree.setFill('white')
        toothThree.setOutline('black')
        toothThree.move(-42,0)
        toothThree.draw(win)

        #left ear
        leftEar = Circle(center,50)
        leftEar.move(249,0)
        leftEar.draw(win)

        #right ear
        rightEar = Circle(center,50)
        rightEar.move(-249,0)
        rightEar.draw(win)

        #hair
        hairone = Line(Point(400,199), Point(400,150))
        hairone.setFill('black')
        hairone.setOutline('black')
        hairone.draw(win)
        
        hairtwo = hairone.clone()
        hairtwo.move(10,0)
        hairtwo.draw(win)
        
        win.getMouse()
        win.close()

main() 


main()