def phoneLoad():  # loads the phone png
    global phone
    phone = loadImage("Phone.png")

def phoneDraw(xPos, yPos):  # draw player phone
    global phone
    # imageMode(CENTER)
    image(phone, xPos, yPos)

"""
def phoneMove(finalX, finalY):
    if gameState == 0:
        yPos = yPos + height
        while yPos > finalY:
            yPos--
"""
# make buttons iterable
class buttonRegistry(type):

    def __iter__(cls):
        return iter(cls._registry)

# function to build buttons
class button(object):  # class defenition
    __metaclass__ = buttonRegistry
    _registry = []

    # object instructor
    def __init__(self, xPos, yPos, buttonWidth, buttonHeight, strokeColour, buttonLabel):
        self._registry.append(self)
        # self.name =
        self.yPos = yPos
        self.xPos = xPos
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.strokeColour = strokeColour
        self.buttonLabel = buttonLabel

    def display(self):  # display method
        buttonAlpha = 100
        # buttonHover()
        alpha(buttonAlpha)
        rectMode(CENTER)
        stroke(self.strokeColour)
        fill(self.strokeColour)
        rect(self.xPos, self.yPos, self.buttonWidth, self.buttonHeight, 7)
        fill(0, 0, 0)
        textSize(30)
        textAlign(CENTER, CENTER)
        text(self.buttonLabel, self.xPos, self.yPos,
             self.buttonWidth - 10, self.buttonHeight - 10)
"""
def buttonHover():
    for i in range(len(_registry)):
        if mouseX < self.xPos + self.buttonWidth/2 and mouseX > self.xPos - self.buttonWidth/2 and mouseY < self.yPos - self.buttonHeight/2 and mouseY > self.yPos + self.buttonHeight/2:
             buttonAlpha = 50
"""
introMenu = 0
introHelp = 1
introGameTransition = 2
mainGame = 3
gameOver = 4
gameState = 0

def gameStateControl(stateValue):
    if stateValue == 0:
        phoneX = 242
        phoneY = 48
        phoneDraw(phoneX, phoneY)

        # set up and display play and help buttons buttons
        buttonColour = color(255, 255, 255)
        #buttonWidth = 190
        #buttonHeight = 75
        playLabel = "PLAY"
        helpLabel = "HELP"
        playButton = button(
            phoneX + phone.width / 2, phoneY + 150, 190, 75, buttonColour, playLabel)
        helpButton = button(
            phoneX + phone.width / 2, phoneY + 250, 190, 75, buttonColour, helpLabel)
        playButton.display()
        helpButton.display()
        
        # button results
        if mousePressed:
            if mouseX > playButton.xPos - playButton.buttonWidth / 2 and mouseX < playButton.xPos + playButton.buttonWidth / 2 and mouseY > playButton.yPos - playButton.buttonHeight / 2 and mouseY < playButton.yPos + playButton.buttonHeight / 2:
                global gameState
                gameState = introGameTransition
            if mouseX > helpButton.xPos - helpButton.buttonWidth / 2 and mouseX < helpButton.xPos + helpButton.buttonWidth / 2 and mouseY > helpButton.yPos - helpButton.buttonHeight / 2 and mouseY < helpButton.yPos + helpButton.buttonHeight / 2:
                global gameState
                gameState = introHelp

    elif stateValue == 1:
        gameState = 0
    elif stateValue == 2:
        gameState = 3

    elif stateValue == 3:
        phoneX = 10
        phoneY = 48
        phoneDraw(phoneX, phoneY)
        
        row = 0
        while row < 4:
            
        

def setup():
    size(800, 600)
    phoneLoad()

def draw():
    background(255, 255, 255)
    gameStateControl(gameState)
