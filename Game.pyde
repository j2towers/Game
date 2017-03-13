
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
    # constructor

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
        self.followerTotal += (fitFollower +
                               hipFollower + lifeFollower + fashFollower)
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

    def __init__(self, name, cost, locationImage, buttonLabel):
        self.name = name
        self.locationImage = locationImage
        self.locationOn = False
        # number of times in a row location has been used
        self.tiredLocation = 0
        self.turnsSinceLocation = 0  # number of turns since location was used
        self.buttonLabel = buttonLabel

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
class buttonRegistry(type):

    def __iter__(cls):
        return iter(cls.btnRegistry)

class button(object):  # class defenition
    # object constructor
    __metaclass__ = buttonRegistry
    btnRegistry = []

    def __init__(self, xPos, yPos, buttonWidth, buttonHeight, strokeColour, buttonLabel, buttonResult, buttonType):
        self.btnRegistry.append(self)
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
    for buttonobject in button:
        b = buttonobject
        if b.buttonType == "gameStateButton" and b.buttonOn == True:
            if mouseX > b.xPos - b.buttonWidth / 2 and mouseX < b.xPos + b.buttonWidth / 2 and mouseY > b.yPos - b.buttonHeight / 2 and mouseY < b.yPos + b.buttonHeight / 2:
                global gameState
                gameState = b.buttonResult
                println(b.buttonLabel)
                println(b.yPos)
                buttonKill()

def buttonKill():
    for buttonobject in button:
        b = buttonobject
        b.buttonOn = False

def introMenuButtonBuild(phoneX, phoneY):
    # set up and display play and help buttons buttons
    buttonColour = color(200, 200, 200)
    buttonX = phoneX + phone.width / 2
    buttonY = phoneY + 268
    helpLabel = "HELP"
    helpButton = button(
        phoneX + phone.width / 2, buttonY, 76, 23, buttonColour, helpLabel, 1, "gameStateButton")
    helpButton.display()
    return(helpButton)

def helpMenuButtonBuild(phoneX, phoneY):
    # set up and display play and help buttons buttons
    buttonColour = color(200, 200, 200)
    buttonX = phoneX + phone.width / 2
    buttonY = phoneY + 250
    playLabel = "PLAY"
    playButton = button(
        phoneX + phone.width / 2, buttonY, 76, 23, buttonColour, playLabel, 3, "gameStateButton")
    playButton.display()
    return(playButton)


def locationButtonBuild(phoneX, phoneY):
    # set up location buttons
    buttonColour = color(200, 200, 200)
    buttonX = phoneX + 355
    buttonY = phoneY + 90
    cafeLabel = "CAFE"
    galleryLabel = "GALLERY"
    bedroomLabel = "BEDROOM"
    natureLabel = "NATURE"
    cityLabel = "CITY"
    studioLabel = "STUDIO"
    cafeButton = button(
        buttonX, buttonY, 43, 43, buttonColour, cafeLabel, 3, "locationButton")
    buttonX += 60
    galleryButton = button(
        buttonX, buttonY, 43, 43, buttonColour, galleryLabel, 3, "locationButton")
    buttonX += 60
    bedroomButton = button(
        buttonX, buttonY, 43, 43, buttonColour, bedroomLabel, 3, "locationButton")
    buttonX += 60
    natureButton = button(
        buttonX, buttonY, 43, 43, buttonColour, natureLabel, 3, "locationButton")
    buttonX += 60
    cityButton = button(
        buttonX, buttonY, 43, 43, buttonColour, cityLabel, 3, "locationButton")
    buttonX += 60
    studioButton = button(
        buttonX, buttonY, 43, 43, buttonColour, studioLabel, 3, "locationButton")
    cafeButton.display()
    galleryButton.display()
    bedroomButton.display()
    natureButton.display()
    cityButton.display()
    studioButton.display()
    return(cafeButton, galleryButton, bedroomButton, natureButton, cityButton, studioButton)

def foodButtonBuild(phoneX, phoneY):
    # set up food buttons
    buttonColour = color(200, 200, 200)
    buttonX = phoneX + 355
    buttonY = phoneY + 157
    coffeeLabel = "COFFEE"
    bagelLabel = "BAGEL"
    croissantLabel = "CROISSANT"
    sandwichLabel = "SANDWICH"
    icecreamLabel = "ICECREAM"
    pizzaLabel = "PIZZA"
    burgerLabel = "BURGER"
    coffeeButton = button(
        buttonX, buttonY, 43, 43, buttonColour, cafeLabel, 3, "locationButton")
    buttonX += 60
    bagelButton = button(
        buttonX, buttonY, 43, 43, buttonColour, galleryLabel, 3, "locationButton")
    buttonX += 60
    bedroomButton = button(
        buttonX, buttonY, 43, 43, buttonColour, bedroomLabel, 3, "locationButton")
    buttonX += 60
    natureButton = button(
        buttonX, buttonY, 43, 43, buttonColour, natureLabel, 3, "locationButton")
    buttonX += 60
    cityButton = button(
        buttonX, buttonY, 43, 43, buttonColour, cityLabel, 3, "locationButton")
    buttonX += 60
    studioButton = button(
        buttonX, buttonY, 43, 43, buttonColour, studioLabel, 3, "locationButton")
    cafeButton.display()
    galleryButton.display()
    bedroomButton.display()
    natureButton.display()
    cityButton.display()
    studioButton.display()
    return(cafeButton, galleryButton, bedroomButton, natureButton, cityButton, studioButton)


def gameStateControl(stateValue):
    if stateValue == 0:
        buttonKill()
        phoneX = width / 2 - phone.width / 2
        phoneY = 46
        phoneDraw(phoneX, phoneY)
        introMenuButtonBuild(phoneX, phoneY)

        # button results
        if mousePressed:
            buttonHittest()

    elif stateValue == 1:
        buttonKill()
        phoneX = width / 2 - phone.width / 2
        phoneY = 46
        phoneDraw(phoneX, phoneY)
        helpMenuButtonBuild(phoneX, phoneY)

        if mousePressed:
            buttonHittest()

    elif stateValue == 2:
        gameState = 3

    elif stateValue == 3:
        phoneX = 29
        phoneY = 46
        phoneDraw(phoneX, phoneY)
        locationButtonBuild(phoneX, phoneY)

    elif stateValue == 4:
        gameState = 0


def setup():
    size(800, 600)
    sponsorBuild()
    pngLoad()

def draw():
    background(255, 255, 255)
    gameStateControl(gameState)
