def phoneLoad():  # loads the phone png
    global phone
    phone = loadImage("Phone.png")

def phoneDraw(xPos, yPos):  # draw player phone
    global phone
    phoneWidth = 417
    phoneHeight = 872
    imageMode(CENTER)
    # pushMatrix()
    # scale(2)
    image(phone, xPos, yPos)
    # popMatrix()
"""
def phoneMove(finalX, finalY):
    if gameState == 0:
        yPos = yPos + height
        while yPos > finalY:
            yPos--
"""

# function to build buttons
class button(object):  # class defenition

    def __init__(self, xPos, yPos, strokeColour):  # object instructor
        self.yPos = yPos
        self.xPos = xPos
        self.strokeColour = strokeColour

    def display(self):  # display method
        noFill()
        rectMode(CENTER)
        stroke(self.strokeColour)

introMenu = 0
intoGameTransition = 1
mainGame = 2
gameOver = 3
gameState = 0

def gameStateControl(stateValue):
    if stateValue == 0:
        phoneX = width / 2
        phoneY = height/ 2
        phoneDraw(phoneX, phoneY)
    elif stateValue == 1:

        gameState = 0
    elif stateValue == 2:
        gameState = 0
    elif stateValue == 3:
        gameState = 0


def setup():
    size(1280, 850)
    phoneLoad()

def draw():
    background(255, 255, 255)
    gameStateControl(gameState)
