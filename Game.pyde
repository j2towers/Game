# constants to avoid magic numbers
from Settings import * 

# gamestates
introMenu = 0
introHelp = 1
introGameTransition = 2
mainGame = 3
gameOver = 4
gameState = 0

# random number maker with a normal distribution from 0 to max
def randomNormal(floorNum, maxNum):
    i = int(map(round(randomGaussian() * 100), -200, 200, floorNum, maxNum))
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

class player(object):
    #constructor
    def __init__(self):
        self.fitFollower = 0
        self.hipFollower = 0
        self.lifeFollower = 0
        self.fashFollower = 0
        self.followerTotal = 0
        self.moneyTotal = 0
        
    def playerUpdate(fitAdd, hipAdd, lifeAdd, fashAdd, moneyAdd):
        self.fitFollower += fitAdd
        self.hipFollower += hipAdd
        self.lifeFollower += lifeAdd
        self.fashFollower += fashAdd
        self.followerTotal += (fitFollower + hipFollower + lifeFollower + fashFollower)
        self.moneyTotal += moneyAdd
        
        

class sponsor(object):  # sponsor class
    moodThresholdMax = 500  # max mood for a sponsor to bring you on
    bonusMax = 500  # max sponsor bonus
    # object constructor
    def __init__(self, name, goodThings, badThings):
        self.sponsoring = False
        self.name = name
        self.mood = -(randomNormal(0, 100))
        self.moodThreshold = randomNormal(0, sponsor.moodThresholdMax)
        self.bonusAmounts = randomNormal(10, self.bonusMax)
        self.bonusFreq = randomNormal(1, 5)
        self.turnsSinceBonus = 0
        self.goodThings = goodThings
        self.badThings = badThings

    def sponsorPay(self):
        if self.sponsoring == True:
            if self.turnsSinceBonus >= self.bonusFreq:
                playerUpdate(0, 0, 0, 0, self.bonusAmount)
        else:
            if self.mood >= self.moodThreshold:
                self.sponsoring = True
            

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
    
    
    for name in sponsorArray.keys():
        if name == "Sportsco":
            sponsorArray[name] = sponsor(name, sportscoGood, sportscoBad)
        elif name == "Kate's Coffee":
            sponsorArray[name] = sponsor(name, coffeeGood, coffeeBad)
        elif name == "Tourism Board":
            sponsorArray[name] = sponsor(name, tourismGood, tourismBad)
        elif name == "Nate's Kitchen":
            sponsorArray[name] = sponsor(name, restaurantGood, restaurantBad)
        elif name == "Fashion Haus":
            sponsorArray[name] = sponsor(name, fashionGood, fashionBad)

def sponsorCheck():
    for sponsorName, sponsor in sponsorArray.iteritems():
        for locationName, location in locationArray.iteritems():
            if locationName in sponsor.goodThings:
                sponsor.mood += randomNormal(0, 200)
            if locationName in sponsor.badThings:
                sponsor.mood -= randomNormal(0, 200)
        for inventoryName, inventory in inventoryArray.iteritems():
            if inventoryName in sponsor.goodThings:
                sponsor.mood += randomNormal(0, 200)
            if inventoryName in sponsor.badThings:
                sponsor.mood -= randomNormal(0, 200)
        sponsor.sponsorPay()
        
        


class audience(object):  # audience class
    # object constructor

    def __init__(self, name, goodThings, badThings):
        self.name = name
        self.amount = 0
        self.goodThings = goodThings
        self.badThings = badThings


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

    def __init__(self, xPos, yPos, buttonWidth, buttonHeight, strokeColour, buttonLabel, buttonResult):
        self.buttonOn = True
        self.yPos = yPos
        self.xPos = xPos
        # self.buttonType = buttonType
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
        if b.buttonType == gameStateButton:
            if mouseX > b.xPos - b.buttonWidth / 2 and mouseX < b.xPos + b.buttonWidth / 2 and mouseY > b.yPos - b.buttonHeight / 2 and mouseY < b.yPos + b.buttonHeight / 2:
                global gameState
                gameState = b.buttonResult

def introMenuButtonBuild(phoneX, phoneY):
            # set up and display play and help buttons buttons
    buttonColour = color(200, 200, 200)
    #buttonWidth = 190
    #buttonHeight = 75
    playLabel = "PLAY"
    helpLabel = "HELP"
    playButton = button(
        phoneX + phone.width / 2, phoneY + 150, 160, 75, buttonColour, playLabel, 3)
    helpButton = button(
        phoneX + phone.width / 2, phoneY + 250, 160, 75, buttonColour, helpLabel, 1)
    playButton.display()
    helpButton.display()
    return(playButton, helpButton)


def gameStateControl(stateValue):
    if stateValue == 0:
        phoneX = 242
        phoneY = 48
        phoneDraw(phoneX, phoneY)
        playButton, helpButton = introMenuButtonBuild(phoneX, phoneY)

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
        playButton, helpButton = introMenuButtonBuild(phoneX, phoneY)

        helpBoxDraw(phoneX + phone.width / 2 - helpBox.width / 2,
                    phoneY + phone.height / 2 - helpBox.height / 2)

        buttonColour = color(255, 255, 255)
        playLabel = "PLAY"

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
        
        text(
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