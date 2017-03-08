# constants to avoid magic numbers
moodThresholdMax = 500  # max mood for a sponsor to bring you on
bonusMax = 1000  # max sponsor bonus
# gamestates
introMenu = 0
introHelp = 1
introGameTransition = 2
mainGame = 3
gameOver = 4
gameState = 0

# random number maker with a normal distribution from 0 to max
def randomNormal(maxNum):
    i = int(map(round(randomGaussian() * 100), -200, 200, 0, maxNum))
    if i < 0:
        i = abs(i)
    return(i)

def pngLoad():  # loads the phone png
    global phone
    phone = loadImage("Phone.png")
    global helpBox
    helpBox = loadImage("Helpbox.png")

def phoneDraw(xPos, yPos):  # draw player phone
    global phone
    image(phone, xPos, yPos)

def helpBoxDraw(xPos, yPos):  # draw help screen box
    global helpBox
    image(helpBox, xPos, yPos)

"""
def phoneMove(finalX, finalY):
    if gameState == 0:
        yPos = yPos + height
        while yPos > finalY:
            yPos--
"""

sponsorArray = ["Sportsco", "Kate's Coffee",
                "Tourism Board", "Nate's Kitchen", "Fashion Haus"]
class sponsor(object):  # sponsor class
    # object constructor

    def __init__(self, name, moodThreshold, bonusAmounts, goodThings, badThings):
        self.sponsored = False
        self.name = name
        self.mood = 0
        self.moodThreshold = moodThreshold
        self.bonusAmounts = bonusAmounts
        self.goodThings = goodThings
        self.badThings = badThings

    def sponsorUpdate(self):
        if self.sponsored == True:

        # update sponsor moods and things here from array of items that are
        # turned on and locations used

def sponsorBuild():
    sportscoGood = [
        "City Scape", "Nature", "Sneakers", "Shirts", "Workout", "Sunglasses"]
    sportscoBad = ["Art Gallery", "Studio", "Casual", "Heels",
                   "Mac", "Camera", "Stationary", "Manicure", "Bag", "Car"]
    coffeeGood = ["Cafe", "Coffee", "Bagel", "Croissant"]
    coffeeBad = ["Sandwich", "Ice Cream", "Pizza", "Burger"]
    tourismGood = ["Art Gallery", "Nature", "City Scape", "Camera"]
    tourismBad = ["Car", "Bedroom"]
    restaurantGood = ["Sandwich", "Ice Cream", "Pizza", "Burger"]
    restaurantBad = ["Cafe", "Coffee", "Bagel", "Croissant"]
    fashionGood = ["T-Shirt", "Casual", "Dressed Up", "Heels"]
    fashionBad = ["Workout", "Sneakers"]
    for i in sponsorArray:
        if i == "Sportsco":
            i = sponsor(i, randomNormal(moodThresholdMax), randomNormal(
                bonusMax), sportscoGood, sportscoBad)
        elif i == "Kate's Coffee":
            i = sponsor(i, randomNormal(moodThresholdMax), randomNormal(
                bonusMax), coffeeGood, coffeeBad)
        elif i == "Tourism Board":
            i = sponsor(i, randomNormal(moodThresholdMax), randomNormal(
                bonusMax), tourismGood, tourismBad)
        elif i == "Nate's Kitchen":
            i = sponsor(i, randomNormal(moodThresholdMax), randomNormal(
                bonusMax), restaurantGood, restaurantBad)
        elif i == "Fashion Haus":
            i = sponsor(i, randomNormal(moodThresholdMax), randomNormal(
                bonusMax), fashionGood, fashionBad)


audienceArray = ["Fitness", "Hipster", "Lifestyle", "Fashion"]
class audience(object):  # audience class
    # object constructor

    def __init__(self, name, goodThings, badThings):
        self.name = name
        self.amount = 0
        self.goodThings = goodThings
        self.badThings = badThings

locationArray = [
    "Cafe", "Art Gallery", "Bedroom", "Nature", "City Scape", "Studio"]
class location(object):  # location class

    def __init__(self, name, cost, locationImage):
        self.name = name
        self.locationImage = locationImage
        self.locationOn = False
        # number of times in a row location has been used
        self.tiredLocation = 0
        self.turnsSinceLocation = 0  # number of turns since location was used
        # todo build some kind of if statement that assigns the location to
        # category or categories

    # def display(self): #location display
        # todo draw stuff here

foodArray = ["Coffee", "Bagel", "Croissant",
             "Sandwich", "Ice Cream", "Pizza", "Burger"]
outfitArray = ["T-Shirt", "Casual", "Dressed Up",
               "Workout", "Sneakers", "Heels", "Hand"]
itemArray = ["Mac", "Camera", "Stationary",
             "Manicure", "Sunglass", "Bag", "Car"]
class inventory(object):  # inventory class

    def __init__(self, name, cost, inventoryImage):
        self.name = name
        self.cost = cost
        self.inventoryImage = inventoryImage
        self.tiredImage = 0  # number of times in a row item has been used
        self.turnsSinceItem = 0  # number of times in a row item has been used
        # todo build some kind of if statement that assigns the item to
        # category or categories

    # def display(self): #item display
        # todo draw stuff here

# function to build buttons
class button(object):  # class defenition
    # object constructor

    def __init__(self, xPos, yPos, buttonWidth, buttonHeight, strokeColour, buttonLabel, buttonResult, buttonType):
        self.buttonOn = True
        self.yPos = yPos
        self.xPos = xPos
        self.buttonType = buttonType
        # todo make this the destination of the button
        self.buttonResult = buttonResult
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.strokeColour = strokeColour
        self.buttonLabel = buttonLabel
        # add to an array of buttons and build hittest that loops over every
        # button in the array

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

def buttonHittest():
    i = 0
    while i < len(buttonArray):
        b = buttonArray[i]
        if b.buttonType == gameStateButton
            if mouseX > b.xPos - b.buttonWidth / 2 and mouseX < b.xPos + b.buttonWidth / 2 and mouseY > b.yPos - b.buttonHeight / 2 and mouseY < b.yPos + b.buttonHeight / 2:
                global gameState
                gameState = b.buttonResult

def introMenuButtonBuild():
            # set up and display play and help buttons buttons
    buttonColour = color(200, 200, 200)
    #buttonWidth = 190
    #buttonHeight = 75
    playLabel = "PLAY"
    helpLabel = "HELP"
    playButton = button(
        phoneX + phone.width / 2, phoneY + 150, 160, 75, buttonColour, playLabel)
    helpButton = button(
        phoneX + phone.width / 2, phoneY + 250, 160, 75, buttonColour, helpLabel)
    playButton.display()
    helpButton.display()


def gameStateControl(stateValue):
    if stateValue == 0:
        phoneX = 242
        phoneY = 48
        phoneDraw(phoneX, phoneY)

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

    elif stateValue == 4:
        gameState = 0


def setup():
    size(800, 600)
    sponsorBuild()
    pngLoad()

def draw():
    background(255, 255, 255)
    gameStateControl(gameState)
