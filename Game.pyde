
from Settings import *

# gamestates
introMenu = 0
introHelp = 1
introGameTransition = 2
mainGame = 3
gameOver = 4
gameState = 0

# roboto load
def fontLoad():
    font = loadFont("Roboto-Regular-14.vlw")
    textAlign(LEFT, TOP)
    textFont(font)


# random number maker with a normal distribution from 0 to max
def randomNormal(floorNum, maxNum):
    i = int(map(round(randomGaussian() * 100), -200, 200, floorNum, maxNum))
    if i < 0:
        i = abs(i)
    return(i)

# load images
def pngLoad(): 
    global phone
    phone = loadImage("Phone.png")
    global helpBox
    helpBox = loadImage("Helpbox.png")
    global logo
    logo = loadImage("Logo.png")
    
    # location buttons
    global bedroom
    bedroom = loadImage("Bedroom.png")
    global cafe
    cafe = loadImage("Cafe.png")
    global cityscape
    cityscape = loadImage("CityScape.png")
    global gallery
    gallery = loadImage("Gallery.png")
    global nature
    nature = loadImage("Nature.png")
    global studio
    studio = loadImage("Studio.png")
    
    # food buttons
    global bagel
    bagel = loadImage("Bagel.png")
    global coffee
    coffee = loadImage("Coffee.png")
    global icecream
    icecream = loadImage("Icecream.png")
    global pastry
    pastry = loadImage("Pastry.png")
    global pizza
    pizza = loadImage("Pizza.png")
    global sandwich
    sandwich = loadImage("Sandwich.png")
    global tea
    tea = loadImage("Tea.png")
    
    #item buttons
    global bag
    bag = loadImage("Bag.png")
    global digicamera
    digicamera = loadImage("Camera.png")
    global car
    car = loadImage("Car.png")
    global laptop
    laptop = loadImage("Laptop.png")
    global manicure
    manicure = loadImage("Manicure.png")
    global shades
    shades = loadImage("Shades.png")
    
    # clothes buttons
    global casual
    casual = loadImage("CasualLook.png")
    global formal
    formal = loadImage("DressedupLook.png")
    global heels
    heels = loadImage("Heels.png")
    global shirts
    shirts = loadImage("Shirts.png")
    global sneakers
    sneakers = loadImage("Sneakers.png")
    global workout
    workout = loadImage("WorkoutLook.png")
    
    # backgrounds
    global bedroomBG
    bedroomBG = loadImage("bedroom-BG.png")
    

# draw phone
def phoneDraw(xPos, yPos): 
    global phone
    image(phone, xPos, yPos)

# draw help screen box
def helpBoxDraw(xPos, yPos):  
    global helpBox
    image(helpBox, xPos, yPos)

# draw daily logo
def logoDraw(xPos, yPos):
    global logo
    image(logo, xPos + phone.width / 2 - logo.width / 2, yPos + 132)


#player class to track game
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
        "City Scape", "Nature", "Sneakers", "Shirts", "Workout", "Shades"]
    sportscoBad = ["Art Gallery", "Studio", "Casual", "Heels",
                   "Laptop", "Camera", "Stationary", "Manicure", "Bag", "Car"]
    coffeeGood = ["Cafe", "Coffee", "Bagel", "Pastry"]
    coffeeBad = ["Sandwich", "Ice Cream", "Pizza"]
    tourismGood = ["Art Gallery", "Nature", "City Scape", "Camera"]
    tourismBad = ["Car", "Bedroom"]
    restaurantGood = ["Sandwich", "Ice Cream", "Pizza"]
    restaurantBad = ["Cafe", "Coffee", "Bagel", "Pastry"]
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


# function to make locations iterable
class locationRegistry(type):

    def __iter__(cls):
        return iter(cls.lcnRegistry)

class location(object):  # location class
    __metaclass__ = locationRegistry
    lcnRegistry = []

    def __init__(self, name, cost, locationImage, buttonLabel):
        self.lcnRegistry.append(self)
        self.name = name
        self.locationImage = locationImage
        self.locationOn = False
        # number of times in a row location has been used
        self.tiredLocation = 0
        self.turnsSinceLocation = 0  # number of turns since location was used
        self.buttonLabel = buttonLabel

    def display(self, phoneX, phoneY): #location display
        locX = phoneX + 43
        locY = phoneY
        if self.locationOn == True:
            image(self.locationImage, phoneX, phoneY)
        # todo draw stuff here

def locationDraw(phoneX, phoneY):
    for locationObject in location:
        loc = locationObject
        loc.display(phoneX, phoneY)
  
def locationBuild():
    for l in locationArray:
        name = l + "location"
        name = location(l, randomNormal(0, 50), l[0], l[1])      

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

# function to make buttons iterable
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
        textSize(10)
        textAlign(CENTER, CENTER)
        text(self.buttonLabel, self.xPos, self.yPos,
             self.buttonWidth - 10, self.buttonHeight - 10)

def buttonHittest():
    onCount = 0
    for buttonobject in button:
        b = buttonobject
        if b.buttonType == "gameStateButton" and b.buttonOn == True:
            if mouseX > b.xPos - b.buttonWidth / 2 and mouseX < b.xPos + b.buttonWidth / 2 and mouseY > b.yPos - b.buttonHeight / 2 and mouseY < b.yPos + b.buttonHeight / 2:
                global gameState
                gameState = b.buttonResult
                println(b.buttonLabel)
                println(b.yPos)
        if b.buttonType == "locationButton" and b.buttonOn == True:
            for locationobject in location:
                l = locationobject
                if l.locationOn == True:
                    onCount += 1
            if onCount == 0:    
                if mouseX > b.xPos - b.buttonWidth / 2 and mouseX < b.xPos + b.buttonWidth / 2 and mouseY > b.yPos - b.buttonHeight / 2 and mouseY < b.yPos + b.buttonHeight / 2:
                    name = b.buttonLabel
                    for locationobject in location:
                        output.print(name)
                        output.print(locationobject.name)
                        if name == locationobject.name:
                            locationobject.locationOn = True
                            println(b.buttonLabel)
                            println(b.yPos)
            elif onCount > 0:
                if mouseX > b.xPos - b.buttonWidth / 2 and mouseX < b.xPos + b.buttonWidth / 2 and mouseY > b.yPos - b.buttonHeight / 2 and mouseY < b.yPos + b.buttonHeight / 2:
                    name = b.buttonLabel
                    for locationobject in location:
                        locationobject.locationOn = False
                        println("turned off")
                        println(onCount)
                        println(b.buttonLabel)
                        println(b.yPos)

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
    buttonColour = color(200, 200, 200, 10)
    buttonX = phoneX + 350
    buttonY = phoneY + 90
    cafeLabel = "Cafe"
    galleryLabel = "GALLERY"
    bedroomLabel = "BEDROOM"
    natureLabel = "NATURE"
    cityLabel = "CITY"
    studioLabel = "STUDIO"
    cafeButton = button(
        buttonX, buttonY, 43, 43, buttonColour, cafeLabel, 3, "locationButton")
    imageX = buttonX - cafeButton.buttonWidth/2
    imageY = buttonY - cafeButton.buttonHeight/2
    image(cafe, imageX, imageY)
    buttonX += 60
    galleryButton = button(
        buttonX, buttonY, 43, 43, buttonColour, galleryLabel, 3, "locationButton")
    imageX = buttonX - cafeButton.buttonWidth/2
    imageY = buttonY - cafeButton.buttonHeight/2
    image(gallery, imageX, imageY)
    buttonX += 60
    bedroomButton = button(
        buttonX, buttonY, 43, 43, buttonColour, bedroomLabel, 3, "locationButton")
    imageX = buttonX - cafeButton.buttonWidth/2
    imageY = buttonY - cafeButton.buttonHeight/2
    image(bedroom, imageX, imageY)
    buttonX += 60
    natureButton = button(
        buttonX, buttonY, 43, 43, buttonColour, natureLabel, 3, "locationButton")
    imageX = buttonX - cafeButton.buttonWidth/2
    imageY = buttonY - cafeButton.buttonHeight/2
    image(nature, imageX, imageY)
    buttonX += 60
    cityButton = button(
        buttonX, buttonY, 43, 43, buttonColour, cityLabel, 3, "locationButton")
    imageX = buttonX - cafeButton.buttonWidth/2
    imageY = buttonY - cafeButton.buttonHeight/2
    image(cityscape, imageX, imageY)
    buttonX += 60
    studioButton = button(
        buttonX, buttonY, 43, 43, buttonColour, studioLabel, 3, "locationButton")
    imageX = buttonX - cafeButton.buttonWidth/2
    imageY = buttonY - cafeButton.buttonHeight/2
    image(studio, imageX, imageY)
    cafeButton.display()
    galleryButton.display()
    bedroomButton.display()
    natureButton.display()
    cityButton.display()
    studioButton.display()
    return(cafeButton, galleryButton, bedroomButton, natureButton, cityButton, studioButton)

def foodButtonBuild(phoneX, phoneY):
    # set up food buttons
    buttonColour = color(200, 200, 200, 10)
    buttonX = phoneX + 350
    buttonY = phoneY + 157
    coffeeLabel = "COFFEE"
    bagelLabel = "BAGEL"
    pastryLabel = "PASTRY"
    sandwichLabel = "SANDWICH"
    icecreamLabel = "ICECREAM"
    pizzaLabel = "PIZZA"
    coffeeButton = button(
        buttonX, buttonY, 43, 43, buttonColour, coffeeLabel, 3, "itemButton")
    imageX = buttonX - coffeeButton.buttonWidth/2
    imageY = buttonY - coffeeButton.buttonHeight/2
    image(coffee, imageX, imageY)
    buttonX += 60
    bagelButton = button(
        buttonX, buttonY, 43, 43, buttonColour, bagelLabel, 3, "itemButton")
    imageX = buttonX - coffeeButton.buttonWidth/2
    imageY = buttonY - coffeeButton.buttonHeight/2
    image(bagel, imageX, imageY)
    buttonX += 60
    pastryButton = button(
        buttonX, buttonY, 43, 43, buttonColour, pastryLabel, 3, "itemButton")
    imageX = buttonX - coffeeButton.buttonWidth/2
    imageY = buttonY - coffeeButton.buttonHeight/2
    image(pastry, imageX, imageY)
    buttonX += 60
    sandwichButton = button(
        buttonX, buttonY, 43, 43, buttonColour, sandwichLabel, 3, "itemButton")
    imageX = buttonX - coffeeButton.buttonWidth/2
    imageY = buttonY - coffeeButton.buttonHeight/2
    image(sandwich, imageX, imageY)
    buttonX += 60
    icecreamButton = button(
        buttonX, buttonY, 43, 43, buttonColour, icecreamLabel, 3, "itemButton")
    imageX = buttonX - coffeeButton.buttonWidth/2
    imageY = buttonY - coffeeButton.buttonHeight/2
    image(icecream, imageX + 10, imageY)
    buttonX += 60
    pizzaButton = button(
        buttonX, buttonY, 43, 43, buttonColour, pizzaLabel, 3, "itemButton")
    imageX = buttonX - coffeeButton.buttonWidth/2
    imageY = buttonY - coffeeButton.buttonHeight/2
    image(pizza, imageX, imageY)
    coffeeButton.display()
    bagelButton.display()
    pastryButton.display()
    sandwichButton.display()
    icecreamButton.display()
    pizzaButton.display()
    return(coffeeButton, bagelButton, pastryButton, sandwichButton, icecreamButton, pizzaButton)

def itemButtonBuild(phoneX, phoneY):
    # set up food buttons
    buttonColour = color(200, 200, 200, 10)
    buttonX = phoneX + 350
    buttonY = phoneY + 224
    laptopLabel = "LAPTOP"
    cameraLabel = "CAMERA"
    manicureLabel = "MANICURE"
    shadesLabel = "SHADES"
    bagLabel = "BAG"
    carLabel = "CAR"
    laptopButton = button(
        buttonX, buttonY, 43, 43, buttonColour, laptopLabel, 3, "itemButton")
    imageX = buttonX - laptopButton.buttonWidth/2
    imageY = buttonY - laptopButton.buttonHeight/2
    image(laptop, imageX, imageY)
    buttonX += 60
    cameraButton = button(
        buttonX, buttonY, 43, 43, buttonColour, cameraLabel, 3, "itemButton")
    imageX = buttonX - laptopButton.buttonWidth/2
    imageY = buttonY - laptopButton.buttonHeight/2
    image(digicamera, imageX, imageY)
    buttonX += 60
    manicureButton = button(
        buttonX, buttonY, 43, 43, buttonColour, manicureLabel, 3, "itemButton")
    imageX = buttonX - laptopButton.buttonWidth/2
    imageY = buttonY - laptopButton.buttonHeight/2
    image(manicure, imageX + 10, imageY)
    buttonX += 60
    shadesButton = button(
        buttonX, buttonY, 43, 43, buttonColour, shadesLabel, 3, "itemButton")
    imageX = buttonX - laptopButton.buttonWidth/2
    imageY = buttonY - laptopButton.buttonHeight/2
    image(shades, imageX, imageY)
    buttonX += 60
    bagButton = button(
        buttonX, buttonY, 43, 43, buttonColour, bagLabel, 3, "itemButton")
    imageX = buttonX - laptopButton.buttonWidth/2
    imageY = buttonY - laptopButton.buttonHeight/2
    image(bag, imageX + 5, imageY)
    buttonX += 60
    carButton = button(
        buttonX, buttonY, 43, 43, buttonColour, carLabel, 3, "itemButton")
    imageX = buttonX - laptopButton.buttonWidth/2
    imageY = buttonY - laptopButton.buttonHeight/2
    image(car, imageX, imageY)
    laptopButton.display()
    cameraButton.display()
    manicureButton.display()
    shadesButton.display()
    bagButton.display()
    carButton.display()
    return(laptopButton, cameraButton, manicureButton, shadesButton, bagButton, carButton)

def outfitButtonBuild(phoneX, phoneY):
    # set up food buttons
    buttonColour = color(200, 200, 200, 10)
    buttonX = phoneX + 350
    buttonY = phoneY + 291
    shirtLabel = "SHIRT"
    casualLabel = "CASUAL"
    dressedUpLabel = "DRESSED UP"
    workoutLabel = "WORKOUT"
    sneakersLabel = "SNEAKERS"
    heelsLabel = "HEELS"
    shirtButton = button(
        buttonX, buttonY, 43, 43, buttonColour, shirtLabel, 3, "itemButton")
    imageX = buttonX - shirtButton.buttonWidth/2
    imageY = buttonY - shirtButton.buttonHeight/2
    image(shirts, imageX, imageY)
    buttonX += 60
    casualButton = button(
        buttonX, buttonY, 43, 43, buttonColour, casualLabel, 3, "itemButton")
    imageX = buttonX - shirtButton.buttonWidth/2
    imageY = buttonY - shirtButton.buttonHeight/2
    image(casual, imageX, imageY)
    buttonX += 60
    dressedUpButton = button(
        buttonX, buttonY, 43, 43, buttonColour, dressedUpLabel, 3, "itemButton")
    imageX = buttonX - shirtButton.buttonWidth/2
    imageY = buttonY - shirtButton.buttonHeight/2
    image(formal, imageX, imageY)
    buttonX += 60
    workoutButton = button(
        buttonX, buttonY, 43, 43, buttonColour, workoutLabel, 3, "itemButton")
    imageX = buttonX - shirtButton.buttonWidth/2
    imageY = buttonY - shirtButton.buttonHeight/2
    image(workout, imageX, imageY)
    buttonX += 60
    sneakersButton = button(
        buttonX, buttonY, 43, 43, buttonColour, sneakersLabel, 3, "itemButton")
    imageX = buttonX - shirtButton.buttonWidth/2
    imageY = buttonY - shirtButton.buttonHeight/2
    image(sneakers, imageX, imageY)
    buttonX += 60
    heelsButton = button(
        buttonX, buttonY, 43, 43, buttonColour, heelsLabel, 3, "itemButton")
    imageX = buttonX - shirtButton.buttonWidth/2
    imageY = buttonY - shirtButton.buttonHeight/2
    image(heels, imageX, imageY)
    shirtButton.display()
    casualButton.display()
    dressedUpButton.display()
    workoutButton.display()
    sneakersButton.display()
    heelsButton.display()
    return(shirtButton, casualButton, dressedUpButton, workoutButton, sneakersButton, heelsButton)

def itemButtonLabels(phoneX, phoneY):
    textX = phoneX + 329
    textY = phoneY + 53
    textSize(14)
    textAlign(LEFT, TOP)
    text("Location", textX, textY)
    textY += 67
    text("Food", textX, textY)
    textY += 67
    text("Items", textX, textY)
    textY += 67
    text("Outfit", textX, textY)
    

def gameStateControl(stateValue):
    if stateValue == 0:
        buttonKill()
        phoneX = width / 2 - phone.width / 2
        phoneY = 46
        phoneDraw(phoneX, phoneY)
        logoDraw(phoneX, phoneY)
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
        foodButtonBuild(phoneX, phoneY)
        itemButtonBuild(phoneX, phoneY)
        outfitButtonBuild(phoneX, phoneY)
        itemButtonLabels(phoneX, phoneY)
        locationDraw(phoneX, phoneY)
        
        if mousePressed:
            buttonHittest()

    elif stateValue == 4:
        gameState = 0


def setup():
    size(800, 600)
    sponsorBuild()
    locationBuild()
    fontLoad()
    pngLoad()
    
    global output
    output = createWriter("log.txt")

def draw():
    background(255, 255, 255)
    gameStateControl(gameState)
    output.flush()