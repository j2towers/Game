def phoneLoad():  # loads the phone png
    global phone
    phone = loadImage("Phone.png")

def phoneDraw(xPos, yPos):  # draw player phone
    global phone
    imageMode(CENTER)
    image(phone, xPos, yPos)

"""
def phoneMove(finalX, finalY):
    if gameState == 0:
        yPos = yPos + height
        while yPos > finalY:
            yPos--
"""
#make buttons iterable
class buttonRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

# function to build buttons
class button(object):  # class defenition
    __metaclass__ = buttonRegistry
    _registry = []

    def __init__(self, xPos, yPos, buttonWidth, buttonHeight, strokeColour, buttonLabel):  # object instructor
        self._registry.append(self)
        #self.name = 
        self.yPos = yPos
        self.xPos = xPos
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.strokeColour = strokeColour
        self.buttonLabel = buttonLabel

    def display(self):  # display method
        buttonAlpha = 100
        alpha(buttonAlpha)
        rectMode(CENTER)
        stroke(self.strokeColour)
        fill(self.strokeColour)
        rect(self.xPos, self.yPos, self.buttonWidth, self.buttonHeight, 7)
        fill(0, 0, 0)
        textSize(30)
        textAlign(CENTER, CENTER)
        text(self.buttonLabel, self.xPos, self.yPos, self.buttonWidth - 10, self.buttonHeight - 10)

def buttonHover():
    for buttonobject in button:
        if mouseX < self.xPos + self.buttonWidth/2 and mouseX > self.xPos - self.buttonWidth/2 and mouseY < self.yPos - self.buttonHeight/2 and mouseY > self.yPos + self.buttonHeight/2:
             buttonAlpha = 50
    
introMenu = 0
intoGameTransition = 1
mainGame = 2
gameOver = 3
gameState = 0

def gameStateControl(stateValue):
    if stateValue == 0:
        phoneX = width / 2
        phoneY = height / 2
        phoneDraw(phoneX, phoneY)
        
        #set up and display buttons
        buttonColour = color(255, 255, 255)
        playLabel = "PLAY"
        helpLabel = "HELP"
        playButton = button(phoneX, phoneY - 100, 200, 75, buttonColour, playLabel)
        helpButton = button(phoneX, phoneY + 50, 200, 75, buttonColour, helpLabel)
        playButton.display()
        helpButton.display()
    elif stateValue == 1:
        gameState = 0
    elif stateValue == 2:
        gameState = 0
    elif stateValue == 3:
        gameState = 0


def setup():
    size(800, 600)
    phoneLoad()

def draw():
    background(255, 255, 255)
    gameStateControl(gameState)
