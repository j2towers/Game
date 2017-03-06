def pngLoad():  # loads the phone png
    global phone
    phone = loadImage("Phone.png")
    global helpBox
    helpBox = loadImage("Helpbox.png")

def phoneDraw(xPos, yPos):  # draw player phone
    global phone
    image(phone, xPos, yPos)

def helpBoxDraw(xPos, yPos): # draw help screen box
    global helpBox
    image(helpBox, xPos, yPos)

"""
def phoneMove(finalX, finalY):
    if gameState == 0:
        yPos = yPos + height
        while yPos > finalY:
            yPos--
"""

sponsorArray = ["Adidas", "Smile Tiger Coffee", "The Art Gallery of Ontario", "Hilton Hotels", "Allan Gardens", "Mildred’s Temple Kitchen", "Studio"]
class sponsor(object): #sponsor class
    #object constructor
    def __init__(self, name, moodThreshold, bonusAmounts, goodThings, badThings):
        self.sponsored = false
        self.name = name
        self.mood = 0
        self.moodThreshold = moodThreshold
        self.bonusAmounts = bonusAmounts
        self.goodThings = goodThings
        self.badThings = badThings

audienceArray = ["Sporty", "Hipster", "Lifestyle", "Fashion"]                
class audience(object): #audience class
    #object constructor
    def __init__(self, name, goodThings, badThings):
        self.name = name
        self.amount = 0
        self.goodThings = goodThings
        self.badThings = badThings
        
locationArray = ["Cafe", "Art Gallery", "Bedroom", "Nature", "City Scape", "Studio"]
class location(object): #location class
    def __init__(self, name, locationImage):
        self.name = name
        self.locationImage = locationImage
        self.locationOn = false 
        self.tiredLocation = 0 #number of times in a row location has been used
        self.turnsSinceLocation = 0 #number of turns since location was used
        #todo build some kind of if statement that assigns the location to category or categories
        
    #def display(self): #location display 
        #todo draw stuff here
        
foodArray = ["Coffee", "Bagel", "Croissant", "Sandwich", "Ice Cream", "Pizza", "Burger"]
outfitArray = ["T-Shirt", "Casual", "Dressed Up", "Workout", "Sneakers", "Heels", "Hand"]
itemArray = ["Mac", "Camera", "Stationary", "Manicure", "Sunglass", "Bag", "Car"]
class inventory(object): #inventory class
    def __init__(self, name, inventoryImage):
        self.name = name
        self.inventoryImage = inventoryImage
        self.tiredImage = 0 #number of times in a row item has been used
        self.turnsSinceItem = 0 #number of times in a row item has been used
        #todo build some kind of if statement that assigns the item to category or categories
        
    #def display(self): #item display
        #todo draw stuff here

# function to build buttons
class button(object):  # class defenition
    # object constructor
    def __init__(self, xPos, yPos, buttonWidth, buttonHeight, strokeColour, buttonLabel):
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

#gamestates
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
        phoneX = 242
        phoneY = 48
        phoneDraw(phoneX, phoneY)

        helpBoxDraw(phoneX + phone.width / 2 - helpBox.width / 2,
                    phoneY + phone.height / 2 - helpBox.height / 2)

        buttonColour = color(255, 255, 255)
        playLabel = "PLAY"

        playButton = button(
            phoneX + phone.width / 2, phoneY + 330, 140, 50, buttonColour, playLabel)
        playButton.display()
        
        if mousePressed:
            if mouseX > playButton.xPos - playButton.buttonWidth / 2 and mouseX < playButton.xPos + playButton.buttonWidth / 2 and mouseY > playButton.yPos - playButton.buttonHeight / 2 and mouseY < playButton.yPos + playButton.buttonHeight / 2:
                global gameState
                gameState = introGameTransition
    
    elif stateValue == 2:
        gameState = 3

    elif stateValue == 3:
        phoneX = 10
        phoneY = 48
        phoneDraw(phoneX, phoneY)
        """
        row = 0
        while row < 4:
        """


def setup():
    size(800, 600)
    pngLoad()

def draw():
    background(255, 255, 255)
    gameStateControl(gameState)
