
from Arrays import *

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
    #println("random: " + "low:" + str(floorNum) + " high:" + str(maxNum) + " result:" + str(i))
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
    global gadget
    gadget = loadImage("Gadget.png")
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
    
    # items
    global coffeePic
    coffeePic = loadImage("coffeePic.png")
    global bagelPic
    bagelPic = loadImage("bagelPic.png")
    global pastryPic
    pastryPic = loadImage("pastryPic.png")
    global sandwichPic
    sandwichPic = loadImage("sandwichPic.png")
    global icecreamPic
    icecreamPic = loadImage("icecreamPic.png")
    global teaPic
    teaPic = loadImage("teaPic.png")
    global gadgetPic
    gadgetPic = loadImage("gadgetPic.png")
    global tabletPic
    tabletPic = loadImage("tabletPic.png")
    global cameraPic
    cameraPic = loadImage("cameraPic.png")
    global manicurePic
    manicurePic = loadImage("manicurePic.png")
    global shadesPic
    shadesPic = loadImage("shadesPic.png")
    global bagPic
    bagPic = loadImage("bagPic.png")
    global carPic
    carPic = loadImage("carPic.png")
    global shirtPic
    shirtPic = loadImage("shirtPic.png")
    global casualPic
    casualPic = loadImage("casualPic.png")
    global formalPic
    formalPic = loadImage("formalPic.png")
    global workoutPic
    workoutPic = loadImage("workoutPic.png")
    global sneakerPic
    sneakerPic = loadImage("sneakerPic.png")
    global heelsPic
    heelsPic = loadImage("heelsPic.png")
   
     # hand mode items
     
    

# draw phone
def phoneDraw(xPos, yPos): 
    global phone
    imageMode(CORNER)
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
        #println(str(self.name) + " " + str(self.mood) + " " + str(self.moodThreshold))
        self.bonusAmount = randomNormal(10, self.bonusMax)
        self.bonusFreq = randomNormal(1, 5)
        self.turnsSinceBonus = 0
        self.goodThings = goodThings
        self.badThings = badThings
        sponsorList.append(self)

    def sponsorPay(self):
        #println(self.name)
        #println("mood: " + str(self.mood))
        #println("moodlimit: " + str(self.moodThreshold))
        #println("sponsoring: " + str(self.sponsoring))
        #println(str(self.turnsSinceBonus) + " " + str(self.bonusFreq))
        self.turnsSinceBonus += 1
        if self.sponsoring == True:
            if self.turnsSinceBonus >= self.bonusFreq:
                self.turnsSinceBonus = 0
                bonus = self.bonusAmount
                playerUpdate(0, 0, 0, 0, bonus)
        else:
            if self.mood >= self.moodThreshold:
                self.sponsoring = True

   

def sponsorBuild():
    println("sponsors built")
    sportscoGood = [
        "City Scape", "Nature", "Sneakers", "Shirts", "Workout", "Shades"]
    sportscoBad = ["Art Gallery", "Wall", "Casual", "Heels",
                   "Gadget", "Camera", "Stationary", "Manicure", "Bag", "Car"]
    coffeeGood = ["Cafe", "Coffee", "Bagel", "Pastry"]
    coffeeBad = ["Sandwich", "Ice Cream", "Tea"]
    tourismGood = ["Art Gallery", "Nature", "City Scape", "Camera"]
    tourismBad = ["Car", "Bedroom"]
    restaurantGood = ["Sandwich", "Ice Cream", "Tea"]
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
        for inventoryitem in itemList:
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
    fitnessBad = ["Bagel", "Croissant", "Sandwich", "Ice Cream", "Tea", "Burger", "Car"]
    lifestyleGood = ["Gallery", "Bedroom", "City", "Dressed Up", "Manicure", "Car"]
    lifestyleBad = ["Sandwich", "Ice Cream", "Tea", "Burger", "Shirt", "Workout"]
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
        for inventoryitem in itemList:
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
        if self.locationImage == bedroomBG:
            image(bedroomBG, self.xPos, self.yPos)
        elif self.locationImage == cafeBG:
            image(cafeBG, self.xPos, self.yPos)
        elif self.locationImage == galleryBG:
            image(galleryBG, self.xPos, self.yPos)
        elif self.locationImage == natureBG:
            image(natureBG, self.xPos, self.yPos)
        elif self.locationImage == cityBG:
            image(cityBG, self.xPos, self.yPos)
        elif self.locationImage == wallBG:
            image(wallBG, self.xPos, self.yPos)
        # todo draw stuff here

def locationDraw(phoneX, phoneY):
    locationX = phoneX + 41
    locationY = phoneY + 70
    for locationObject in locationList:
        locationObject.xPos = locationX
        locationObject.yPos = locationY
        if locationObject.locationOn == True:  
            imageMode(CORNER)      
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

class item(object):  # inventory class

    def __init__(self, name, cost, handMode, itemImage, buttonLabel):
        self.xPos = 0
        self.yPos = 0
        self.name = name
        self.cost = cost
        self.bought = False
        self.handMode = handMode
        self.itemImage = itemImage
        self.itemOn = False
        # number of times in a row location has been used
        self.tiredItem = 0
        self.buttonLabel = buttonLabel
        itemList.append(self)
        
    def display(self): #item display
        if self.itemImage == coffeePic:
            image(coffeePic, self.xPos, self.yPos)
        elif self.itemImage == bagelPic:
            image(bagelPic, self.xPos, self.yPos)
        elif self.itemImage == pastryPic:
            image(pastryPic, self.xPos, self.yPos)
        elif self.itemImage == sandwichPic:
            image(sandwichPic, self.xPos, self.yPos)
        elif self.itemImage == icecreamPic:
            image(icecreamPic, self.xPos, self.yPos)
        elif self.itemImage == teaPic:
            image(teaPic, self.xPos, self.yPos)
        elif self.itemImage == gadgetPic:
            image(gadgetPic, self.xPos, self.yPos)
        elif self.itemImage == cameraPic:
            image(cameraPic, self.xPos, self.yPos)
        elif self.itemImage == manicurePic:
            image(manicurePic, self.xPos, self.yPos)
        elif self.itemImage == shadesPic:
            image(shadesPic, self.xPos, self.yPos)
        elif self.itemImage == bagPic:
            image(bagPic, self.xPos, self.yPos)
        elif self.itemImage == carPic:
            image(carPic, self.xPos, self.yPos)
        elif self.itemImage == shirtPic:
            image(shirtPic, self.xPos, self.yPos)
        elif self.itemImage == casualPic:
            image(casualPic, self.xPos, self.yPos)
        elif self.itemImage == formalPic:
            image(formalPic, self.xPos, self.yPos)
        elif self.itemImage == workoutPic:
            image(workoutPic, self.xPos, self.yPos)
        elif self.itemImage == sneakerPic:
            image(sneakerPic, self.xPos, self.yPos)
        elif self.itemImage == heelsPic:
            image(heelsPic, self.xPos, self.yPos)
            
def itemDraw(phoneX, phoneY):
    itemX = phoneX + 41
    itemY = phoneY + 70
    for itemObject in itemList:
        itemObject.xPos = itemX
        itemObject.yPos = itemY
        if itemObject.itemOn == True:        
            imageMode(CORNER)
            itemObject.display()
        else:
            continue
  
def itemBuild():
    coffee = item("Coffee", randomNormal(1, 7), 0, coffeePic, "coffeeButton")
    bagel = item("Bagel", randomNormal(1, 4), 0, bagelPic, "bagelButton")
    pastry = item("Pastry", randomNormal(1, 4), 0, pastryPic, "pastryLabel")
    sandwich = item("Sandwich", randomNormal(5, 10), 0, sandwichPic, "sandwichLabel")
    icecream = item("IceCream", randomNormal(1, 5), 0, icecreamPic, "icecreamLabel")
    tea = item("Tea", randomNormal(1, 5), 0, teaPic, "teaLabel")
    gadget = item("Gadget", randomNormal(300, 700), 0, gadgetPic, "gadgetLabel")
    digicamera = item("Camera", randomNormal(100, 300), 0, cameraPic, "cameraLabel")
    manicure = item("Manicure", randomNormal(10, 30), 0, manicurePic, "manicureLabel")
    shades = item("Shades", randomNormal(10, 100), 0, shadesPic, "shadesLabel")
    bag = item("Bag", randomNormal(50, 100), 0, bagPic, "bagLabel")
    car = item("Car", randomNormal(80, 200), 0, carPic, "carLabel")
    shirt = item("Shirt", randomNormal(10, 50), 0, shirtPic, "shirtLabel")
    casual = item("Casual", randomNormal(30, 70), 0, casualPic, "casualLabel")
    formal = item("Formal", randomNormal(50, 150), 0, formalPic, "formalLabel")
    workout = item("Workout", randomNormal(20, 70), 0, workoutPic, "wourkoutLabel")
    sneakers = item("Sneakers", randomNormal(50, 150), 0, sneakerPic, "sneakerLabel")
    heels = item("Heels", randomNormal(100, 200), 0, heelsPic, "heelsLabel")



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
    for inventoryitem in itemList:
        i = inventoryitem
        i.itemOn = False
    println("ding")


def buttonHittest():
    println("Start")
    for buttonobject in buttonList:
        b = buttonobject
        if mouseX > b.xPos - b.buttonWidth / 2 and mouseX < b.xPos + b.buttonWidth / 2 and mouseY > b.yPos - b.buttonHeight / 2 and mouseY < b.yPos + b.buttonHeight / 2:
            println(b.buttonType == "snapButton" and b.buttonOn == True)
            if b.buttonType == "gameStateButton" and b.buttonOn == True:
                global gameState
                gameState = b.buttonResult
                #println(b.buttonLabel)
                #println(b.yPos)
            elif b.buttonType == "locationButton" and b.buttonOn == True:
                for locationobject in locationList:
                    l = locationobject
                    if l.name == b.buttonLabel:
                        l.locationOn = True
                    elif l.name != b.buttonLabel:
                        l.locationOn = False
            elif b.buttonType == "itemButton" or "foodButton" or "outfitButton" and b.buttonOn == True:
                for itemobject in itemList:
                    i = itemobject
                    if i.name == b.buttonLabel:
                        #println(i.itemOn)
                        i.itemOn = not i.itemOn
                        #println("result: " + str(i.itemOn))
                    else:
                        continue
            elif b.buttonType == "snapButton" and b.buttonOn == True:
                println("snapmatch")
                snapButton()   
        else:
            continue
    println("End")
                        
                

def buttonKill():
    for buttonobject in buttonList:
        b = buttonobject
        buttonList.remove(b)


def introMenuButtonBuild():
    # set up and display play and help buttons buttons
    buttonColour = color(200, 200, 200)
    buttonX = 0
    buttonY = 0
    helpLabel = "HELP"
    helpButton = button(
        buttonX, buttonY, 76, 23, buttonColour, helpLabel, 1, "gameStateButton")

def introMenuButtonDisplay(phoneX, phoneY):
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "HELP":
            b.xPos = phoneX + phone.width / 2
            b.yPos = phoneY + 268
            b.display()


def helpMenuButtonBuild():
    # set up and display play and help buttons buttons
    buttonColour = color(200, 200, 200)
    buttonX = 0
    buttonY = 0
    playLabel = "PLAY"
    playButton = button(
        buttonX, buttonY, 76, 23, buttonColour, playLabel, 3, "gameStateButton")

def helpMenuButtonDisplay(phoneX, phoneY):
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "PLAY":
            b.xPos = phoneX + phone.width / 2
            b.yPos = phoneY + 200
            b.display()
            

def locationButtonBuild():
    # set up location buttons
    buttonColour = color(200, 200, 200, 10)
    buttonX = 0
    buttonY = 0
    cafeLabel = "Cafe"
    galleryLabel = "Gallery"
    bedroomLabel = "Bedroom"
    natureLabel = "Nature"
    cityLabel = "City"
    wallLabel = "Wall"
    cafeButton = button(
        buttonX, buttonY, 43, 43, buttonColour, cafeLabel, 3, "locationButton")
    galleryButton = button(
        buttonX, buttonY, 43, 43, buttonColour, galleryLabel, 3, "locationButton")
    bedroomButton = button(
        buttonX, buttonY, 43, 43, buttonColour, bedroomLabel, 3, "locationButton")
    natureButton = button(
        buttonX, buttonY, 43, 43, buttonColour, natureLabel, 3, "locationButton")
    cityButton = button(
        buttonX, buttonY, 43, 43, buttonColour, cityLabel, 3, "locationButton")
    wallButton = button(
        buttonX, buttonY, 43, 43, buttonColour, wallLabel, 3, "locationButton")

def locationButtonDisplay(phoneX, phoneY):    
    buttonX = phoneX + 350
    buttonY = phoneY + 90
    for buttonItem in buttonList:
        b = buttonItem 
        if b.buttonType == "locationButton":
            b.xPos = buttonX
            b.yPos = buttonY
            imageMode(CENTER)
            if b.buttonLabel == "Cafe":
                image(cafe, b.xPos, b.yPos)
            elif b.buttonLabel == "Gallery":
                image(gallery, b.xPos, b.yPos)
            elif b.buttonLabel == "Bedroom":
                image(bedroom, b.xPos, b.yPos)
            elif b.buttonLabel == "Nature":
                image(nature, b.xPos, b.yPos)
            elif b.buttonLabel == "City":
                image(cityscape, b.xPos, b.yPos)
            elif b.buttonLabel == "Wall":
                image(wall, b.xPos, b.yPos)
            b.display()
            buttonX += 60
 

def foodButtonBuild():
    # set up food buttons
    buttonColour = color(200, 200, 200, 10)
    buttonX = 0
    buttonY = 0
    coffeeLabel = "Coffee"
    bagelLabel = "Bagel"
    pastryLabel = "Pastry"
    sandwichLabel = "Sandwich"
    icecreamLabel = "IceCream"
    teaLabel = "Tea"
    coffeeButton = button(
        buttonX, buttonY, 43, 43, buttonColour, coffeeLabel, 3, "foodButton")
    bagelButton = button(
        buttonX, buttonY, 43, 43, buttonColour, bagelLabel, 3, "foodButton")
    pastryButton = button(
        buttonX, buttonY, 43, 43, buttonColour, pastryLabel, 3, "foodButton")
    sandwichButton = button(
        buttonX, buttonY, 43, 43, buttonColour, sandwichLabel, 3, "foodButton")
    icecreamButton = button(
        buttonX, buttonY, 43, 43, buttonColour, icecreamLabel, 3, "foodButton")
    teaButton = button(
        buttonX, buttonY, 43, 43, buttonColour, teaLabel, 3, "foodButton")

def foodButtonDisplay(phoneX, phoneY):
    buttonX = phoneX + 350
    buttonY = phoneY + 157
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonType == "foodButton":
            b.xPos = buttonX
            b.yPos = buttonY
            imageMode(CENTER)
            if b.buttonLabel == "Coffee":
                image(coffee, b.xPos, b.yPos)
            elif b.buttonLabel == "Bagel":
                image(bagel, b.xPos, b.yPos)
            elif b.buttonLabel == "Pastry":
                image(pastry, b.xPos, b.yPos)
            elif b.buttonLabel == "Sandwich":
                image(sandwich, b.xPos, b.yPos)
            elif b.buttonLabel == "IceCream":
                image(icecream, b.xPos, b.yPos)
            elif b.buttonLabel == "Tea":
                image(tea, b.xPos, b.yPos)
            b.display()    
            buttonX += 60
    
    
def itemButtonBuild():
    # set up food buttons
    buttonColour = color(200, 200, 200, 10)
    buttonX = 0
    buttonY = 0
    gadgetLabel = "Gadget"
    cameraLabel = "Camera"
    manicureLabel = "Manicure"
    shadesLabel = "Shades"
    bagLabel = "Bag"
    carLabel = "Car"
    gadgetButton = button(
        buttonX, buttonY, 43, 43, buttonColour, gadgetLabel, 3, "itemButton")
    cameraButton = button(
        buttonX, buttonY, 43, 43, buttonColour, cameraLabel, 3, "itemButton")
    manicureButton = button(
        buttonX, buttonY, 43, 43, buttonColour, manicureLabel, 3, "itemButton")
    shadesButton = button(
        buttonX, buttonY, 43, 43, buttonColour, shadesLabel, 3, "itemButton")
    bagButton = button(
        buttonX, buttonY, 43, 43, buttonColour, bagLabel, 3, "itemButton")
    carButton = button(
        buttonX, buttonY, 43, 43, buttonColour, carLabel, 3, "itemButton")

def itemButtonDisplay(phoneX, phoneY):
    buttonX = phoneX + 350
    buttonY = phoneY + 224
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonType == "itemButton":
            b.xPos = buttonX
            b.yPos = buttonY
            imageMode(CENTER)
            if b.buttonLabel == "Gadget":
                image(gadget, b.xPos, b.yPos)
            elif b.buttonLabel == "Camera":
                image(digicamera, b.xPos, b.yPos)
            elif b.buttonLabel == "Manicure":
                image(manicure, b.xPos, b.yPos)
            elif b.buttonLabel == "Shades":
                image(shades, b.xPos, b.yPos)
            elif b.buttonLabel == "Bag":
                image(bag, b.xPos, b.yPos)
            elif b.buttonLabel == "Car":
                image(car, b.xPos, b.yPos)
            b.display()
            buttonX += 60


def outfitButtonBuild():
    # set up food buttons
    buttonColour = color(200, 200, 200, 10)
    buttonX = 0
    buttonY = 0
    shirtLabel = "Shirt"
    casualLabel = "Casual"
    formalLabel = "Formal"
    workoutLabel = "Workout"
    sneakersLabel = "Sneakers"
    heelsLabel = "Heels"
    shirtButton = button(
        buttonX, buttonY, 43, 43, buttonColour, shirtLabel, 3, "outfitButton")
    casualButton = button(
        buttonX, buttonY, 43, 43, buttonColour, casualLabel, 3, "outfitButton")
    formalButton = button(
        buttonX, buttonY, 43, 43, buttonColour, formalLabel, 3, "outfitButton")
    workoutButton = button(
        buttonX, buttonY, 43, 43, buttonColour, workoutLabel, 3, "outfitButton")
    sneakersButton = button(
        buttonX, buttonY, 43, 43, buttonColour, sneakersLabel, 3, "outfitButton")
    heelsButton = button(
        buttonX, buttonY, 43, 43, buttonColour, heelsLabel, 3, "outfitButton")
    
def outfitButtonDisplay(phoneX, phoneY):
    buttonX = phoneX + 350
    buttonY = phoneY + 291
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonType == "outfitButton":
            b.xPos = buttonX
            b.yPos = buttonY
            imageMode(CENTER)
            if b.buttonLabel == "Shirt":
                image(shirts, b.xPos, b.yPos)
            elif b.buttonLabel == "Casual":
                image(casual, b.xPos, b.yPos)
            elif b.buttonLabel == "Formal":
                image(formal, b.xPos, b.yPos)
            elif b.buttonLabel == "Workout":
                image(workout, b.xPos, b.yPos)
            elif b.buttonLabel == "Sneakers":
                image(sneakers, b.xPos, b.yPos)
            elif b.buttonLabel == "Heels":
                image(heels, b.xPos, b.yPos)
            b.display()
            buttonX += 60
    
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
    
    
def snapButtonBuild():
    buttonX = 0
    buttonY = 0
    snapLabel = "SNAP"
    buttonColour = color(200, 200, 200, 100)
    snapButton = button(buttonX, buttonY, 49, 49, buttonColour, snapLabel, 3, "snapButton")

def snapButtonDisplay(phoneX, phoneY):
    buttonX = phoneX + phone.width / 2
    buttonY = phoneY + 320
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "SNAP":
            b.xPos = buttonX
            b.yPos = buttonY
            fill(200, 200, 200)
            ellipse(b.xPos, b.yPos, 49, 49)
            buttonColour = color(255, 255, 255)
            fill(buttonColour)
            ellipse(b.xPos, b.yPos, 31, 31)
            b.display()
            

#ALL OF THE BUTTON THINGS ARE FINISHED        
    

def gameStateControl(stateValue):
    if stateValue == 0:
        phoneX = width / 2 - phone.width / 2
        phoneY = 46
        phoneDraw(phoneX, phoneY)
        logoDraw(phoneX, phoneY)
        introMenuButtonDisplay(phoneX, phoneY)
        

    elif stateValue == 1:
        phoneX = width / 2 - phone.width / 2
        phoneY = 46
        phoneDraw(phoneX, phoneY)
        helpMenuButtonDisplay(phoneX, phoneY)

    elif stateValue == 2:
        gameState = 3

    elif stateValue == 3:
        phoneX = 29
        phoneY = 46
        #main phone draw
        phoneDraw(phoneX, phoneY)
        
        #button draws
        locationButtonDisplay(phoneX, phoneY)
        foodButtonDisplay(phoneX, phoneY)
        itemButtonDisplay(phoneX, phoneY)
        outfitButtonDisplay(phoneX, phoneY)
        itemButtonLabels(phoneX, phoneY)
        snapButtonDisplay(phoneX, phoneY)
        
        #
        moneyDisplay(phoneX, phoneY)
        locationDraw(phoneX, phoneY)
        itemDraw(phoneX, phoneY)

    elif stateValue == 4:
        gameState = 0

def mouseClicked():
    buttonHittest()
    

def setup():
    size(800, 600)
    
    #asset loads
    fontLoad()
    pngLoad()
    
    #object builds
    sponsorBuild()
    audienceBuild()
    locationBuild()
    itemBuild()
    player()
    
    #button builds
    introMenuButtonBuild()
    helpMenuButtonBuild()
    locationButtonBuild()
    foodButtonBuild()
    itemButtonBuild()
    outfitButtonBuild()
    snapButtonBuild()



def draw():
    background(255, 255, 255)
    gameStateControl(gameState)