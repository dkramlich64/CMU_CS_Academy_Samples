def drawFruit(xCenter, yCenter):
    Oval(xCenter-30, yCenter, 160, 200, fill='crimson')
    Oval(xCenter+30, yCenter, 160, 200, fill='crimson')

def drawStem(stemX, stemY):
    Line(stemX, stemY, stemX-30, stemY-60, fill='peru', lineWidth=8)

def drawLeaf(stemX, stemY):
    Oval(stemX, stemY, 20, 50, fill='seaGreen', rotateAngle=45)


def drawApple(x, y):
    drawLeaf(x, y-150)
    drawStem(x+4, y-85)
    drawFruit(x, y)

drawApple(200, 250)
