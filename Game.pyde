
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
    font = loadFont("Roboto-Regular-48.vlw")
    textAlign(LEFT, TOP)
    textFont(font)


# random number maker with a normal distribution from 0 to max
def randomNormal(floorNum, maxNum):
    i = int(map(round(randomGaussian() * 100), -200, 200, floorNum, maxNum))
    if i < 0:
        i = abs(i)
    if i > maxNum:
        i = maxNum
    println("random: " + "low:" + str(floorNum) + " high:" + str(maxNum) + " result:" + str(i))
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
    global wall
    wall = loadImage("Wall.png")
    
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
    bedroomBG = loadImage("bedroomBG.png")
    global cafeBG
    cafeBG = loadImage("cafeBG.png")
    global cityBG
    cityBG = loadImage("cityBG.png")
    global galleryBG
    galleryBG = loadImage("galleryBG.png")
    global wallBG
    wallBG = loadImage("wallBG.png")
    global natureBG
    natureBG = loadImage("natureBG.png")

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


#PLAYER STUFF

#player class to track game
class player(object):
    # constructor

    def __init__(self):
        self.fitFollower = 0
        self.hipFollower = 0
        self.lifeFollower = 0
        self.fashFollower = 0
        self.followerTotal = 0
        self.moneyTotal = 200
        playerList.append(self)

def playerUpdate(fitAdd, hipAdd, lifeAdd, fashAdd, moneyAdd):
    for playeritem in playerList:
        p = playeritem
        p.fitFollower += fitAdd
        p.hipFollower += hipAdd
        p.lifeFollower += lifeAdd
        p.fashFollower += fashAdd
        p.followerTotal += (p.fitFollower +
                               p.hipFollower + p.lifeFollower + p.fashFollower)
        p.moneyTotal += moneyAdd
        println("money:" + str(p.moneyTotal))
        
def moneyDisplay(phoneX, phoneY):
    moneytextX = phoneX + 330
    followtextX = phoneX + 675
    sponsortextX = (moneytextX + followtextX) / 2
    textY = phoneY + 450
    for playerobject in playerList:
        p = playerobject
        #if p.moneyTotal < 
        money = str(p.moneyTotal)
        textAlign(LEFT)
        textSize(25)
        fill(192, 177, 177)
        text("$" + money, moneytextX, textY)
        textSize(20)
        textAlign(RIGHT)
        text("Followers", followtextX, textY) 
        textAlign(CENTER)
        text("Sponsors", sponsortextX, textY)

    
#SPONSOR STUFF

class sponsor(object):  # sponsor class
    moodThresholdMax = 500  # max mood for a sponsor to bring you on
    bonusMax = 500  # max sponsor bonus
    # object constructor

    def __init__(self, name, goodThings, badThings):
        self.sponsoring = False
        self.name = name
        self.mood = -(randomNormal(0, 50))
        self.moodThreshold = randomNormal(0, self.moodThresholdMax)
        println(str(self.name) + " " + str(self.mood) + " " + str(self.moodThreshold))
        self.bonusAmount = randomNormal(10, self.bonusMax)
        self.bonusFreq = randomNormal(1, 5)
        self.turnsSinceBonus = 0
        self.goodThings = goodThings
        self.badThings = badThings
        sponsorList.append(self)

    def sponsorPay(self):
        println(self.name)
        println("mood: " + str(self.mood))
        println("moodlimit: " + str(self.moodThreshold))
        println("sponsoring: " + str(self.sponsoring))
        println(str(self.turnsSinceBonus) + " " + str(self.bonusFreq))
        self.turnsSinceBonus += 1
        if self.sponsoring == True:
            if self.turnsSinceBonus >= self.bonusFreq:
                self.turnsSinceBonus = 0
                bonus = self.bonusAmount
                playerUpdate(0, 0, 0, 0, bonus)
        else:
            if self.mood >= self.moodThreshold:
                self.sponsoring = True

        # update sponsor moods and things here from array of items that are
        # turned on and locations used

def sponsorBuild():
    println("sponsors built")
    sportscoGood = [
        "City Scape", "Nature", "Sneakers", "Shirts", "Workout", "Shades"]
    sportscoBad = ["Art Gallery", "Wall", "Casual", "Heels",
                   "Laptop", "Camera", "Stationary", "Manicure", "Bag", "Car"]
    coffeeGood = ["Cafe", "Coffee", "Bagel", "Pastry"]
    coffeeBad = ["Sandwich", "Ice Cream", "Pizza"]
    tourismGood = ["Art Gallery", "Nature", "City Scape", "Camera"]
    tourismBad = ["Car", "Bedroom"]
    restaurantGood = ["Sandwich", "Ice Cream", "Pizza"]
    restaurantBad = ["Cafe", "Coffee", "Bagel", "Pastry"]
    fashionGood = ["T-Shirt", "Casual", "Dressed Up", "Heels"]
    fashionBad = ["Workout", "Sneakers"]

    sports = sponsor("Sportsco", sportscoGood, sportscoBad)
    coffee = sponsor("Kate's Coffee", coffeeGood, coffeeBad)
    tourism = sponsor("Tourism Board", tourismGood, tourismBad)
    restaurant = sponsor("Nate's Kitchen", restaurantGood, restaurantBad)
    fashion = sponsor("Fashion Haus", fashionGood, fashionBad)


def sponsorCheck():
    println("sponsorcheck")
    for sponsoritem in sponsorList:
        s = sponsoritem
        for locationitem in locationList:
            l = locationitem
            if l.name in s.goodThings:
                s.mood += randomNormal(0, 50)
            elif l.name in s.badThings:
                s.mood -= randomNormal(0, 50)
            else:
                continue
        for inventoryitem in inventoryList:
            i = inventoryitem
            if i.name in s.goodThings:
                s.mood += randomNormal(0, 50)
            elif i.name in s.badThings:
                s.mood -= randomNormal(0, 50)
            else:
                continue
        s.sponsorPay()


#AUDIENCE STUFF

class audience(object):  # audience class

    # object constructor

    def __init__(self, name, goodThings, badThings):
        self.name = name
        self.amount = 0
        self.goodThings = goodThings
        self.badThings = badThings
        audienceList.append(self)
        
def audienceBuild():
    println("audience built")
    
    hipsterGood = ["Cafe", "Gallery", "City", "Studio", "Coffee", "Croissant", "Casual", "Camera", "Stationary"]
    hipsterBad = ["Dressed Up", "Workout", "Heels", "Hand", "Manicure", "Car"]
    fitnessGood = ["Nature", "Workout", "Sneakers"]
    fitnessBad = ["Bagel", "Croissant", "Sandwich", "Ice Cream", "Pizza", "Burger", "Car"]
    lifestyleGood = ["Gallery", "Bedroom", "City", "Dressed Up", "Manicure", "Car"]
    lifestyleBad = ["Sandwich", "Ice Cream", "Pizza", "Burger", "Shirt", "Workout"]
    fashionGood = ["Gallery", "City", "Dressed Up", "Sneakers", "Heels", "Sunglasses", "Bag"]
    fashionBad = ["Shirt", "Casual", "Workout"]
    
    fitness = audience("Fitness", fitnessGood, fitnessBad)
    hipster = audience("Hipster", hipsterGood, hipsterBad)
    lifestyle = audience("Lifestyle", lifestyleGood, lifestyleBad)
    fashion = audience("Fashion", fashionGood, fashionBad)
    

def audienceCheck():
    fitAdd = 0
    hipAdd = 0
    lifeAdd = 0
    fashAdd = 0
    println("audiencecheck")
    for audienceitem in audienceList:
        a = audienceitem
        a.amount = 0
        for locationitem in locationList:
            l = locationitem
            if l.name in a.goodThings:
                a.amount += randomNormal(0, 200)
            elif l.name in a.badThings:
                a.amount -= randomNormal(0, 200)
            else:
                continue
        for inventoryitem in inventoryList:
            i = inventoryitem
            if i.name in a.goodThings:
                a.amount += randomNormal(0, 200)
            elif i.name in a.badThings:
                a.amount -= randomNormal(0, 200)
            else:
                continue
        if a.name == "Fitness":
            fitAdd = a.amount
        elif a.name == "Hipster":
            hipAdd = a.amount
        elif a.name == "Lifestyle":
            lifeAdd = a.amount
        elif a.name == "Fashion":
            fashAdd = a.amount
            
    playerUpdate(fitAdd, hipAdd, lifeAdd, fashAdd, 0)
    for playeritem in playerList:
        p = playeritem
        println("player stats // Fit: " + str(p.fitFollower) + " Hip: " + str(p.hipFollower) + " Life: " + str(p.lifeFollower) + " Fash: " + str(p.fashFollower) + " Tot: " + str(p.followerTotal))
                


#LOCATION STUFF

class location(object):  # location class

    def __init__(self, xPos, yPos, name, locationImage, buttonLabel):
        self.xPos = xPos
        self.yPos = yPos
        self.name = name
        self.cost = randomNormal(10, 50)
        self.locationImage = locationImage
        self.locationOn = False
        # number of times in a row location has been used
        self.tiredLocation = 0
        self.buttonLabel = buttonLabel
        locationList.append(self)

    def display(self): #location display
        picSize = 191
        if self.locationImage == bedroomBG:
            image(bedroomBG, self.xPos, self.yPos, picSize, picSize)
        elif self.locationImage == cafeBG:
            image(cafeBG, self.xPos, self.yPos, picSize, picSize)
        elif self.locationImage == galleryBG:
            image(galleryBG, self.xPos, self.yPos)
        #elif self.locationImage == natureBG:
         #   image(natureBG, self.xPos, self.yPos, picSize, picSize)
        elif self.locationImage == cityBG:
            image(cityBG, self.xPos, self.yPos, picSize, picSize)
        elif self.locationImage == wallBG:
            image(wallBG, self.xPos, self.yPos, picSize, picSize)
        # todo draw stuff here

def locationDraw(phoneX, phoneY):
    locationX = phoneX + 40
    locationY = phoneY + 70
    for locationObject in locationList:
        locationObject.xPos = locationX
        locationObject.yPos = locationY
        if locationObject.locationOn == True:        
            locationObject.display()
        else:
            continue
  
def locationBuild():
    #locationX = phoneX + 40
    #locationY = phoneY + 70
    cafe = location(0, 0, "Cafe", cafeBG, "cafeButton")
    gallery = location(0, 0, "Gallery", galleryBG, "galleryButton")
    bedroom = location(0, 0, "Bedroom", bedroomBG, "bedroomButton")
    nature = location(0, 0, "Nature", natureBG, "natureButton")
    city = location(0, 0, "City", cityBG, "cityButton")
    wall = location(0, 0, "Wall", wallBG, "wallButton")
        

#LOCATION STUFF

class inventory(object):  # inventory class

    def __init__(self, name, cost, inventoryImage):
        self.name = name
        self.cost = cost
        self.inventoryImage = inventoryImage
        self.tiredImage = 0  # number of times in a row item has been used
        self.turnsSinceItem = 0  # number of times in a row item has been used
        # todo build some kind of if statement that assigns the item to
        # category or categories

#ALL OF THE BUTTON STUFF STARTS HERE

class button(object):  # class defenition

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
        buttonList.append(self)
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


def snapButton():
    sponsorCheck()
    audienceCheck()
    for locationitem in locationList:
        l = locationitem
        l.locationOn = False
    for inventoryitem in inventoryList:
        i = inventoryitem
        i.itemOn = False
    println("ding")


def buttonHittest():
    for buttonobject in buttonList:
        b = buttonobject
        if mouseX > b.xPos - b.buttonWidth / 2 and mouseX < b.xPos + b.buttonWidth / 2 and mouseY > b.yPos - b.buttonHeight / 2 and mouseY < b.yPos + b.buttonHeight / 2:
            if b.buttonType == "gameStateButton" and b.buttonOn == True:
                global gameState
                gameState = b.buttonResult
                println(b.buttonLabel)
                println(b.yPos)
            elif b.buttonType == "locationButton" and b.buttonOn == True:
                for locationobject in locationList:
                    l = locationobject
                    if l.name == b.buttonLabel:
                        l.locationOn = True
                    elif l.name != b.buttonLabel:
                        l.locationOn = False
            elif b.buttonType == "snapButton" and b.buttonOn == True:
                snapButton()   
        else:
            continue
                        
                

def buttonKill():
    for buttonobject in buttonList:
        b = buttonobject
        buttonList.remove(b)

def introMenuButtonBuild(phoneX, phoneY):
    # set up and display play and help buttons buttons
    buttonColour = color(200, 200, 200)
    buttonX = phoneX + phone.width / 2
    buttonY = phoneY + 268
    helpLabel = "HELP"
    helpButton = button(
        buttonX, buttonY, 76, 23, buttonColour, helpLabel, 1, "gameStateButton")
    helpButton.display()
    return(helpButton)

def helpMenuButtonBuild(phoneX, phoneY):
    # set up and display play and help buttons buttons
    buttonColour = color(200, 200, 200)
    buttonX = phoneX + phone.width / 2
    buttonY = phoneY + 250
    playLabel = "PLAY"
    playButton = button(
        buttonX, buttonY, 76, 23, buttonColour, playLabel, 3, "gameStateButton")
    playButton.display()
    return(playButton)


def locationButtonBuild(phoneX, phoneY):
    # set up location buttons
    buttonColour = color(200, 200, 200, 10)
    buttonX = phoneX + 350
    buttonY = phoneY + 90
    cafeLabel = "Cafe"
    galleryLabel = "Gallery"
    bedroomLabel = "Bedroom"
    natureLabel = "Nature"
    cityLabel = "City"
    wallLabel = "Wall"
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
    wallButton = button(
        buttonX, buttonY, 43, 43, buttonColour, wallLabel, 3, "locationButton")
    imageX = buttonX - cafeButton.buttonWidth/2
    imageY = buttonY - cafeButton.buttonHeight/2
    image(wall, imageX, imageY)
    cafeButton.display()
    galleryButton.display()
    bedroomButton.display()
    natureButton.display()
    cityButton.display()
    wallButton.display()
    return(cafeButton, galleryButton, bedroomButton, natureButton, cityButton, wallButton)

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
    
def snapButtonBuild(phoneX, phoneY):
    buttonX = phoneX + phone.width / 2
    buttonY = phoneY + 320
    snapLabel = "SNAP"
    buttonColour = color(200, 200, 200)
    snapButton = button(buttonX, buttonY, 49, 49, buttonColour, snapLabel, 3, "snapButton")
    fill(buttonColour)
    ellipse(buttonX, buttonY, 49, 49)
    buttonColour = color(255, 255, 255)
    fill(buttonColour)
    ellipse(buttonX, buttonY, 31, 31)
    return(snapButton)

#ALL OF THE BUTTON THINGS ARE FINISHED        
    

def gameStateControl(stateValue):
    if stateValue == 0:
        buttonKill()
        phoneX = width / 2 - phone.width / 2
        phoneY = 46
        phoneDraw(phoneX, phoneY)
        logoDraw(phoneX, phoneY)
        introMenuButtonBuild(phoneX, phoneY)

    elif stateValue == 1:
        buttonKill()
        phoneX = width / 2 - phone.width / 2
        phoneY = 46
        phoneDraw(phoneX, phoneY)
        helpMenuButtonBuild(phoneX, phoneY)

    elif stateValue == 2:
        gameState = 3

    elif stateValue == 3:
        buttonKill()
        phoneX = 29
        phoneY = 46
        phoneDraw(phoneX, phoneY)
        locationButtonBuild(phoneX, phoneY)
        #locationBuild(29, 46)
        foodButtonBuild(phoneX, phoneY)
        itemButtonBuild(phoneX, phoneY)
        outfitButtonBuild(phoneX, phoneY)
        itemButtonLabels(phoneX, phoneY)
        snapButtonBuild(phoneX, phoneY)
        moneyDisplay(phoneX, phoneY)
        locationDraw(phoneX, phoneY)


    elif stateValue == 4:
        gameState = 0

def mouseClicked():
    buttonHittest()
    

def setup():
    size(800, 600)
    fontLoad()
    pngLoad()
    sponsorBuild()
    audienceBuild()
    locationBuild()
    player()

    
    
    #global output
    #output = createWriter("log.txt")

def draw():
    background(255, 255, 255)
    gameStateControl(gameState)
    #output.flush()