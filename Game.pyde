  
add_library("sound")

from Arrays import *

#sound
def soundLoad():
    global click
    click = SoundFile(this, "camera.wav")


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
    #game items
    global phone
    phone = loadImage("Phone.png")
    global helpBox
    helpBox = loadImage("Helpbox.png")
    global logo
    logo = loadImage("Logo.png")
    global selfie
    selfie = loadImage("selfie.png")
    global hand
    hand = loadImage("hand.png")
    global thumb
    thumb = loadImage("thumb.png")
    global helpBox
    helpBox = loadImage("Instruction.png")
    global endMode
    endMode = loadImage("endmode.png")
    global instructions
    instructions = loadImage("instructionbutton.png")
    
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
    global blanket
    blanket = loadImage("blanket.png")
    global cafeBG
    cafeBG = loadImage("cafeBG.png")
    global tabletop
    tabletop = loadImage("tabletop.png")
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
    global coffeePic2
    coffeePic2 = loadImage("coffeePic2.png")
    global coffeePicH
    coffeePicH = loadImage("coffeePicH.png")
    global bagelPic
    bagelPic = loadImage("bagelPic.png")
    global bagelPic2
    bagelPic2 = loadImage("bagelPic2.png")
    global bagelPicH
    bagelPicH = loadImage("bagelPicH.png")
    global pastryPic
    pastryPic = loadImage("pastryPic.png")
    global pastryPic2
    pastryPic2 = loadImage("pastryPic2.png")
    global pastryPicH
    pastryPicH = loadImage("pastryPicH.png")
    global sandwichPic
    sandwichPic = loadImage("sandwichPic.png")
    global sandwichPic2
    sandwichPic2 = loadImage("sandwichPic2.png")
    global sandwichPicH
    sandwichPicH = loadImage("sandwichPicH.png")
    global icecreamPic
    icecreamPic = loadImage("icecreamPic.png")
    global icecreamPic2
    icecreamPic2 = loadImage("icecreamPic2.png")
    global icecreamPicH
    icecreamPicH = loadImage("icecreamPicH.png")
    global teaPic
    teaPic = loadImage("teaPic.png")
    global teaPic2
    teaPic2 = loadImage("teaPic2.png")
    global teaPicH
    teaPicH = loadImage("teaPicH.png")
    global gadgetPic
    gadgetPic = loadImage("gadgetPic.png")
    global gadgetPic2
    gadgetPic2 = loadImage("gadgetPic2.png")
    global gadgetPicH
    gadgetPicH = loadImage("gadgetPicH.png")
    global cameraPic
    cameraPic = loadImage("cameraPic.png")
    global cameraPic2
    cameraPic2 = loadImage("cameraPic2.png")
    global cameraPicH
    cameraPicH = loadImage("cameraPicH.png")
    global manicurePic
    manicurePic = loadImage("manicurePic.png")
    global manicurePic2 
    manicurePic2 = loadImage("manicurePic2.png")
    global manicurePicH
    manicurePicH = loadImage("manicurePicH.png")
    global shadesPic
    shadesPic = loadImage("shadesPic.png")
    global shadesPic2
    shadesPic2 = loadImage("shadesPic2.png")
    global shadesPicH
    shadesPicH = loadImage("shadesPicH.png")
    global bagPic
    bagPic = loadImage("bagPic.png")
    global bagPic2
    bagPic2 = loadImage("bagPic2.png")
    global bagPicH
    bagPicH = loadImage("bagPicH.png")
    global carPic
    carPic = loadImage("carPic.png")
    global carPic2
    carPic2 = loadImage("carPic2.png")
    global carPicH
    carPicH = loadImage("carPicH.png")
    global shirtPic
    shirtPic = loadImage("shirtPic.png")
    global shirtPic2
    shirtPic2 = loadImage("shirtPic2.png")
    global shirtPicH
    shirtPicH = loadImage("shirtPicH.png")
    global casualPic
    casualPic = loadImage("casualPic.png")
    global casualPic2
    casualPic2 = loadImage("casualPic2.png")
    global casualPicH
    casualPicH = loadImage("casualPicH.png")
    global formalPic
    formalPic = loadImage("formalPic.png")
    global formalPic2
    formalPic2 = loadImage("formalPic2.png")
    global formalPicH
    formalPicH = loadImage("formalPicH.png")
    global workoutPic
    workoutPic = loadImage("workoutPic.png")
    global workoutPic2
    workoutPic2 = loadImage("workoutPic2.png")
    global workoutPicH
    workoutPicH = loadImage("workoutPicH.png")
    global sneakerPic
    sneakerPic = loadImage("sneakerPic.png")
    global sneakerPic2
    sneakerPic2 = loadImage("sneakerPic2.png")
    global sneakerPicH
    sneakerPicH = loadImage("sneakerPicH.png")
    global heelsPic
    heelsPic = loadImage("heelsPic.png")
    global heelsPic2
    heelsPic2 = loadImage("heelsPic2.png")
    global heelsPicH
    heelsPicH = loadImage("heelsPicH.png")
     
    

# draw phone
def phoneDraw(xPos, yPos): 
    imageMode(CORNER)
    image(phone, xPos, yPos)

# draw help screen box
def helpBoxDraw(xPos, yPos): 
    imageMode(CORNER) 
    image(helpBox, xPos, yPos)

# draw daily logo
def logoDraw(xPos, yPos):
    image(logo, xPos + phone.width / 2 - logo.width / 2, yPos + 132)
 
#hand draw
def handDraw(phoneX, phoneY):
    for modeitem in modeList:
        m = modeitem
        if m.handMode:
            image(hand, phoneX + 41, phoneY + 70)
    
#thumb draw
def thumbDraw(phoneX, phoneY):
    for modeitem in modeList:
        m = modeitem
        if m.handMode:
            image(thumb, phoneX + 41, phoneY + 70)
            
#handmode manicure draw
def tmDraw(phoneX, phoneY):
    for item in itemList:
        i = item
        for modeitem in modeList:
            m = modeitem
            if i.name == "Manicure" and i.itemOn and m.handMode:
                image(manicurePicH, phoneX + 41, phoneY + 70)
            
#draw blanket or tabletop
def bedcafeDraw(phoneX, phoneY):
    for modeitem in modeList:
        m = modeitem
        if m.bedcafeMode and m.handMode == False:
            for locationitem in locationList:
                l = locationitem
                if l.locationOn:
                    if l.name == "Cafe":
                        image(tabletop, phoneX + 41, phoneY + 70)
                    elif l.name == "Bedroom":
                        image(blanket, phoneX + 41, phoneY + 70)

#game over splash draw
def gameOverDraw(phoneX, phoneY):
    imageMode(CENTER)
    image(endMode, phoneX, phoneY)
    textX = width / 2
    textY = phoneY - 125
    textSize(25)
    fill(192, 177, 177)
    textAlign(CENTER)
    text("Congrats! You finished with", textX, textY)
    textY += 35
    for playeritem in playerList:
        p = playeritem
        text("$" + str(p.moneyTotal), textX, textY)
        textY += 35
        text(str(p.followerTotal) + " Followers", textX, textY)
        textY += 35
        mostPop = p.fitFollower
        if p.hipFollower > mostPop:
            mostPop = p.hipFollower
        if p.lifeFollower > mostPop:
            mostPop = p.lifeFollower
        if p.fashFollower > mostPop:
            mostPop = p.fashFollower
        if mostPop == p.fitFollower:
            text("Most popular with fitness fans", textX, textY)
        elif mostPop == p.hipFollower:
            text("Most popular with hipsters", textX, textY)
        elif mostPop == p.lifeFollower:
            text("Most popular with lifestyle fans", textX, textY)
        elif mostPop == p.fashFollower:
            text("Most popular with fashionistas", textX, textY)
        textY += 35
        sponsorCount = 0
        for sponsoritem in sponsorList:
            s = sponsoritem
            if s.sponsoring:
                sponsorCount += 1
        text(str(sponsorCount) + " Sponsors", textX, textY)
        textY += 35
        if sponsorCount > 0:
            for sponsoritem in sponsorList:
                s = sponsoritem
                if s.sponsoring:
                    text(str(s.name), textX, textY)
                    textY += 35
    

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
        self.turnsLeft = 10
        self.moneyTotal = 200
        playerList.append(self)

def playerUpdate(fitAdd, hipAdd, lifeAdd, fashAdd, moneyAdd):
    for playeritem in playerList:
        p = playeritem
        p.fitFollower = max(0, p.fitFollower + fitAdd)
        p.hipFollower = max(0, p.hipFollower + hipAdd)
        p.lifeFollower = max(0, p.lifeFollower + lifeAdd)
        p.fashFollower = max(0, p.fashFollower + fashAdd)
        p.followerTotal = max(0, p.fitFollower + p.hipFollower + p.lifeFollower + p.fashFollower)
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
        
def cashUpdate(cash):
    for playeritem in playerList:
        p = playeritem
        p.moneyTotal = cash
        

#SPONSOR STUFF

class sponsor(object):  # sponsor class
    moodThresholdMax = 300  # max mood for a sponsor to bring you on
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
        self.turnsSinceBonus += 1
        if self.sponsoring == True:
            if self.turnsSinceBonus >= self.bonusFreq:
                self.turnsSinceBonus = 0
                bonus = self.bonusAmount
                playerUpdate(0, 0, 0, 0, bonus)
        else:
            if self.mood >= self.moodThreshold:
                self.sponsoring = True

   
def sponsorMouseOver():
    for sponsoritem in sponsorList:
        s = sponsoritem
        
    
def sponsorBuild():
    println("sponsors built")
    sportscoGood = [
        "City Scape", "Nature", "Sneakers", "Shirts", "Workout", "Shades"]
    sportscoBad = ["Casual", "Heels", "Bagel", "Pastry", "Ice Cream", "Car"]
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
                a.amount += randomNormal(0, 100)
            elif l.name in a.badThings:
                a.amount -= randomNormal(0, 100)
            else:
                continue
        for inventoryitem in itemList:
            i = inventoryitem
            if i.name in a.goodThings:
                a.amount += randomNormal(0, 100)
            elif i.name in a.badThings:
                a.amount -= randomNormal(0, 100)
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

    def __init__(self, xPos, yPos, name, cost, locationImage, buttonLabel):
        self.xPos = xPos
        self.yPos = yPos
        self.name = name
        self.cost = cost
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
    cafe = location(0, 0, "Cafe", randomNormal(1, 5), cafeBG, "cafeButton")
    gallery = location(0, 0, "Gallery", randomNormal(5, 20), galleryBG, "galleryButton")
    bedroom = location(0, 0, "Bedroom", 0, bedroomBG, "bedroomButton")
    nature = location(0, 0, "Nature", randomNormal(5, 20), natureBG, "natureButton")
    city = location(0, 0, "City", randomNormal(5, 20), cityBG, "cityButton")
    wall = location(0, 0, "Wall", randomNormal(1, 5), wallBG, "wallButton")
        

#LOCATION STUFF

class item(object):  # inventory class

    def __init__(self, name, cost, handMode, itemImage, buttonLabel, itemType):
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
        self.itemType = itemType
        itemList.append(self)
        
    def display(self): #item display
        for modeitem in modeList:
            m = modeitem
            if m.handMode:
                if self.itemImage == coffeePic:
                    image(coffeePicH, self.xPos, self.yPos)
                elif self.itemImage == bagelPic:
                    image(bagelPicH, self.xPos, self.yPos)
                elif self.itemImage == pastryPic:
                    image(pastryPicH, self.xPos, self.yPos)
                elif self.itemImage == sandwichPic:
                    image(sandwichPicH, self.xPos, self.yPos)
                elif self.itemImage == icecreamPic:
                    image(icecreamPicH, self.xPos, self.yPos)
                elif self.itemImage == teaPic:
                    image(teaPicH, self.xPos, self.yPos)
                elif self.itemImage == gadgetPic:
                    image(gadgetPicH, self.xPos, self.yPos)
                elif self.itemImage == cameraPic:
                    image(cameraPicH, self.xPos, self.yPos)
                elif self.itemImage == manicurePic:
                    image(manicurePicH, self.xPos, self.yPos)
                elif self.itemImage == shadesPic:
                    image(shadesPicH, self.xPos, self.yPos)
                elif self.itemImage == bagPic:
                    image(bagPicH, self.xPos, self.yPos)
                elif self.itemImage == carPic:
                    image(carPicH, self.xPos, self.yPos)
                elif self.itemImage == shirtPic:
                    image(shirtPicH, self.xPos, self.yPos)
                elif self.itemImage == casualPic:
                    image(casualPicH, self.xPos, self.yPos)
                elif self.itemImage == formalPic:
                    image(formalPicH, self.xPos, self.yPos)
                elif self.itemImage == workoutPic:
                    image(workoutPicH, self.xPos, self.yPos)
                elif self.itemImage == sneakerPic:
                    image(sneakerPicH, self.xPos, self.yPos)
                elif self.itemImage == heelsPic:
                    image(heelsPicH, self.xPos, self.yPos)
            elif m.bedcafeMode:    
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
            else:
                if self.itemImage == coffeePic:
                    image(coffeePic2, self.xPos, self.yPos)
                elif self.itemImage == bagelPic:
                    image(bagelPic2, self.xPos, self.yPos)
                elif self.itemImage == pastryPic:
                    image(pastryPic2, self.xPos, self.yPos)
                elif self.itemImage == sandwichPic:
                    image(sandwichPic2, self.xPos, self.yPos)
                elif self.itemImage == icecreamPic:
                    image(icecreamPic2, self.xPos, self.yPos)
                elif self.itemImage == teaPic:
                    image(teaPic2, self.xPos, self.yPos)
                elif self.itemImage == gadgetPic:
                    image(gadgetPic2, self.xPos, self.yPos)
                elif self.itemImage == cameraPic:
                    image(cameraPic2, self.xPos, self.yPos)
                elif self.itemImage == manicurePic:
                    image(manicurePic2, self.xPos, self.yPos)
                elif self.itemImage == shadesPic:
                    image(shadesPic2, self.xPos, self.yPos)
                elif self.itemImage == bagPic:
                    image(bagPic2, self.xPos, self.yPos)
                elif self.itemImage == carPic:
                    image(carPic2, self.xPos, self.yPos)
                elif self.itemImage == shirtPic:
                    image(shirtPic2, self.xPos, self.yPos)
                elif self.itemImage == casualPic:
                    image(casualPic2, self.xPos, self.yPos)
                elif self.itemImage == formalPic:
                    image(formalPic2, self.xPos, self.yPos)
                elif self.itemImage == workoutPic:
                    image(workoutPic2, self.xPos, self.yPos)
                elif self.itemImage == sneakerPic:
                    image(sneakerPic2, self.xPos, self.yPos)
                elif self.itemImage == heelsPic:
                    image(heelsPic2, self.xPos, self.yPos)
            
def itemDraw(phoneX, phoneY):
    itemX = phoneX + 41
    itemY = phoneY + 70
    for itemObject in itemList:
        itemObject.xPos = itemX
        itemObject.yPos = itemY
        if itemObject.itemOn == True and itemObject.itemType != "Food" and itemObject.itemType != "Clothes":        
            imageMode(CORNER)
            itemObject.display()
        else:
            continue

def charfoodDraw(phoneX, phoneY):
    itemX = phoneX + 41
    itemY = phoneY + 70
    for itemObject in itemList:
        itemObject.xPos = itemX
        itemObject.yPos = itemY
        if itemObject.itemOn == True and itemObject.itemType != "Item" and itemObject.itemType != "Shoes":        
            imageMode(CORNER)
            itemObject.display()
        else:
            continue
    
def itemBuild():
    coffee = item("Coffee", randomNormal(1, 7), 0, coffeePic, "coffeeButton", "Food")
    bagel = item("Bagel", randomNormal(1, 4), 0, bagelPic, "bagelButton", "Food")
    pastry = item("Pastry", randomNormal(1, 4), 0, pastryPic, "pastryLabel", "Food")
    sandwich = item("Sandwich", randomNormal(5, 10), 0, sandwichPic, "sandwichLabel", "Food")
    icecream = item("IceCream", randomNormal(1, 5), 0, icecreamPic, "icecreamLabel", "Food")
    tea = item("Tea", randomNormal(1, 5), 0, teaPic, "teaLabel", "Food")
    gadget = item("Gadget", randomNormal(300, 700), 0, gadgetPic, "gadgetLabel", "Item")
    digicamera = item("Camera", randomNormal(100, 300), 0, cameraPic, "cameraLabel", "Item")
    manicure = item("Manicure", randomNormal(10, 30), 0, manicurePic, "manicureLabel", "Item")
    shades = item("Shades", randomNormal(10, 100), 0, shadesPic, "shadesLabel", "Item")
    bag = item("Bag", randomNormal(50, 100), 0, bagPic, "bagLabel", "Item")
    car = item("Car", randomNormal(80, 200), 0, carPic, "carLabel", "Item")
    shirt = item("Shirt", randomNormal(10, 50), 0, shirtPic, "shirtLabel", "Clothes")
    casual = item("Casual", randomNormal(30, 70), 0, casualPic, "casualLabel", "Clothes")
    formal = item("Formal", randomNormal(50, 150), 0, formalPic, "formalLabel", "Clothes")
    workout = item("Workout", randomNormal(20, 70), 0, workoutPic, "wourkoutLabel", "Clothes")
    sneakers = item("Sneakers", randomNormal(50, 150), 0, sneakerPic, "sneakerLabel", "Shoes")
    heels = item("Heels", randomNormal(100, 200), 0, heelsPic, "heelsLabel", "Shoes")


class gameMode(object):
    
    def __init__(self):
        self.handMode = False
        self.bedcafeMode = False
        self.locationOn = False
        self.outfitOn = False
        self.itemOn = False
        self.foodOn = False
        modeList.append(self)
        


#ALL OF THE BUTTON STUFF STARTS HERE

class button(object):  # class defenition

    def __init__(self, xPos, yPos, buttonWidth, buttonHeight, strokeColour, buttonLabel, buttonResult, buttonType):
        self.buttonOn = False
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
        #text(self.buttonLabel, self.xPos, self.yPos,
             #self.buttonWidth - 10, self.buttonHeight - 10)    


def buttonHittest():
    cash = 0
    for playeritem in playerList:
        p = playeritem
        cash = p.moneyTotal
    for buttonobject in buttonList:
        b = buttonobject
        if mouseX > b.xPos - b.buttonWidth / 2 and mouseX < b.xPos + b.buttonWidth / 2 and mouseY > b.yPos - b.buttonHeight / 2 and mouseY < b.yPos + b.buttonHeight / 2:
            if b.buttonType == "gameStateButton" and b.buttonOn:
                global gameState
                gameState = b.buttonResult
            elif b.buttonType == "gameOverButton" and b.buttonOn:
                if b.buttonLabel == "CONTINUE":
                    for playeritem in playerList:
                        p = playeritem
                        p.turnsLeft = 500
                        global gameState
                        gameState = b.buttonResult
                elif b.buttonLabel == "RESTART":
                    global gameState
                    gameState = b.buttonResult
                    for playeritem in playerList:
                        p = playeritem
                        p.fitFollower = 0
                        p.hipFollower = 0
                        p.lifeFollower = 0
                        p.fashFollower = 0
                        p.followerTotal = 0
                        p.turnsLeft = 10
                        p.moneyTotal = 200
                    for sponsor in sponsorList:
                        s = sponsor
                        s.sponsoring = False
                        s.mood = -(randomNormal(0, 50))
                        s.moodThreshold = randomNormal(0, s.moodThresholdMax)
                        s.bonusAmount = randomNormal(10, s.bonusMax)
                        s.bonusFreq = randomNormal(1, 5)
                        s.turnsSinceBonus = 0
                    for modeitem in modeList:
                        m = modeitem
                        m.handMode = False
                        m.bedcafeMode = False
                        m.locationOn = False
                        m.outfitOn = False
                        m.itemOn = False
                        m.foodOn = False
                    for item in itemList:
                        i = item
                        i.itemOn = False
                        i.bought = False
            elif b.buttonType == "locationButton" and b.buttonOn:
                for locationobject in locationList:
                    l = locationobject
                    if l.name == b.buttonLabel:
                        if l.cost < cash and l.locationOn == False:
                            cash -= l.cost
                            l.locationOn = True
                            cashUpdate(cash)
                            if l.name == "Cafe" or l.name == "Bedroom":
                                for item in itemList:
                                    if item.itemType == "Shoes":
                                        if item.bought:
                                            item.itemOn = False
                                        elif item.itemOn:
                                            cash += item.cost
                                            item.itemOn = False
                                            cashUpdate(cash)
                            for modeitem in modeList:
                                m = modeitem
                                m.locationOn = True
                                if l.name == "Cafe" or l.name == "Bedroom":
                                    m.bedcafeMode = True
                                else:
                                    m.bedcafeMode = False
                    elif l.name != b.buttonLabel:
                        if l.locationOn == True:
                            cash += l.cost
                            l.locationOn = False
                            cashUpdate(cash)
            elif b.buttonType == "outfitButton" and b.buttonOn:
                for modeitem in modeList:
                    m = modeitem
                    if m.locationOn:
                        for itemobject in itemList:
                            i = itemobject
                            if i.name == b.buttonLabel and m.handMode == False:
                                if i.bought:
                                    i.itemOn = True
                                    m.outfitOn = True
                                elif i.cost < cash and i.itemOn == False:
                                    cash -= i.cost
                                    i.itemOn = True
                                    cashUpdate(cash)
                                    m.outfitOn = True
                            elif i.name != b.buttonLabel and i.itemType == "Clothes" and m.handMode == False:
                                if i.itemOn:
                                    cash += i.cost
                                    i.itemOn = False
                                    cashUpdate(cash)
                            elif i.name == b.buttonLabel and m.handMode:
                                if i.bought:
                                    i.itemOn = True
                                    m.outfitOn = True
                                elif i.cost < cash and i.itemOn == False:
                                    cash -= i.cost
                                    i.itemOn = True
                                    cashUpdate(cash)
                                    m.outfitOn = True
                            elif i.name != b.buttonLabel and m.handMode:
                                if i.itemOn:
                                    cash += i.cost
                                    i.itemOn = False
                                    cashUpdate(cash)
            elif b.buttonType == "shoeButton" and b.buttonOn:
                for modeitem in modeList:
                    m = modeitem
                    println(str(m.locationOn) + str(m.outfitOn) + str(m.bedcafeMode) + str(m.handMode))
                    if m.locationOn and m.outfitOn and m.bedcafeMode == False and m.handMode == False:
                        for itemobject in itemList:
                            i = itemobject
                            if i.name == b.buttonLabel:
                                if i.bought:
                                    i.itemOn = not i.itemOn
                                elif i.cost < cash and i.itemOn == False:
                                    cash -= i.cost
                                    i.itemOn = True
                                    cashUpdate(cash)
                                elif i.bought == False and i.itemOn == True:
                                    cash += i.cost
                                    i.itemOn = False
                                    cashUpdate(cash)
                            elif i.name != b.buttonLabel and i.itemType == "Shoes":
                                if i.itemOn:
                                    cash += i.cost
                                    i.itemOn = False
                                    cashUpdate(cash)
                    if m.locationOn and m.handMode:
                        for itemobject in itemList:
                            i = itemobject
                            if i.name == b.buttonLabel:
                                if i.bought:
                                    i.itemOn = True
                                elif i.cost < cash and i.itemOn == False:
                                    cash -= i.cost
                                    i.itemOn = True
                                    cashUpdate(cash)
                            elif i.name != b.buttonLabel:
                                if i.itemOn:
                                    cash += i.cost
                                    i.itemOn = False
                                    cashUpdate(cash)
            elif b.buttonType == "itemButton" and b.buttonOn:
                for modeitem in modeList:
                    m = modeitem
                    #println(str(m.locationOn) + " " + str(m.out)
                    if m.locationOn and m.outfitOn:
                        for itemobject in itemList:
                            i = itemobject
                            if i.name == b.buttonLabel and m.handMode == False:
                                if i.bought:
                                    i.itemOn = True
                                elif i.cost < cash and i.itemOn == False:
                                    cash -= i.cost
                                    i.itemOn = True
                                    cashUpdate(cash)
                            elif i.name != b.buttonLabel and i.itemType == "Item" and m.handMode == False:
                                if i.itemOn and i.bought:
                                    i.itemOn = False 
                                elif i.itemOn:
                                    cash += i.cost
                                    i.itemOn = False
                                    cashUpdate(cash)
                            elif i.name == b.buttonLabel and m.handMode:
                                if i.bought:
                                    i.itemOn = True
                                elif i.cost < cash and i.itemOn == False:
                                    cash -= i.cost
                                    i.itemOn = True
                                    cashUpdate(cash)
                            elif i.name != b.buttonLabel and m.handMode:
                                if i.itemOn and i.bought:
                                    i.itemOn = False
                                elif i.itemOn:
                                    cash += i.cost
                                    i.itemOn = False
                                    cashUpdate(cash)
            elif b.buttonType == "foodButton" and b.buttonOn:
                for modeitem in modeList:
                    m = modeitem
                    #println(str(m.locationOn) + " " + str(m.out)
                    if m.locationOn and m.outfitOn:
                        for itemobject in itemList:
                            i = itemobject
                            if i.name == b.buttonLabel:
                                if i.bought:
                                    i.itemOn = True
                                elif i.cost < cash and i.itemOn == False:
                                    cash -= i.cost
                                    i.itemOn = True
                                    cashUpdate(cash)
                            elif i.name != b.buttonLabel and i.itemType == "Food":
                                if i.itemOn:
                                    cash += i.cost
                                    i.itemOn = False
                                    cashUpdate(cash)
                            elif i.name == b.buttonLabel and m.handMode:
                                if i.bought:
                                    i.itemOn = True
                                elif i.cost < cash and i.itemOn == False:
                                    cash -= i.cost
                                    i.itemOn = True
                                    cashUpdate(cash)
                            elif i.name != b.buttonLabel and m.handMode:
                                if i.itemOn:
                                    cash += i.cost
                                    i.itemOn = False
                                    cashUpdate(cash)
            elif b.buttonType == "handmodeButton" and b.buttonOn:
                for modeitem in modeList:
                    m = modeitem
                    if m.locationOn:
                        if m.handMode:
                            m.handMode = False
                            m.outfitOn = False
                            for item in itemList:
                                i = item
                                i.itemOn = False
                        else:
                            m.handMode = True
                            m.outfitOn = True
                            for item in itemList:
                                i = item
                                i.itemOn = False
            elif b.buttonType == "snapButton" and b.buttonOn:
                for modeitem in modeList:
                    m = modeitem
                    if m.locationOn:
                        snapButton()
                        click.play()   
        else:
            continue


def buttonMouseOver():
    for buttonobject in buttonList:
        b = buttonobject
        xPos = mouseX + 30
        yPos = mouseY - 10
        if mouseX > b.xPos - b.buttonWidth / 2 and mouseX < b.xPos + b.buttonWidth / 2 and mouseY > b.yPos - b.buttonHeight / 2 and mouseY < b.yPos + b.buttonHeight / 2:
            if b.buttonType == "locationButton" and b.buttonOn:
                for locationobject in locationList:
                    l = locationobject
                    if l.name == b.buttonLabel:
                        price = l.cost
                        textSize(14)
                        fill(0, 0, 0)
                        text("$" + str(price) + ".00", xPos, yPos)            
            elif b.buttonType == "itemButton" and b.buttonOn:
                for itemobject in itemList:
                    i = itemobject
                    if i.name == b.buttonLabel and i.bought == False:
                        price = i.cost
                        textSize(14)
                        fill(0, 0, 0)
                        text("$" + str(price) + ".00", xPos, yPos)  
            elif b.buttonType == "foodButton" and b.buttonOn:
                for foodobject in itemList:
                    f = foodobject
                    if f.name == b.buttonLabel:
                        price = f.cost
                        textSize(14)
                        fill(0, 0, 0)
                        text("$" + str(price) + ".00", xPos, yPos)  
            elif b.buttonType == "outfitButton" or b.buttonType == "shoeButton" and b.buttonOn:
                for outfitobject in itemList:
                    o = outfitobject
                    if o.name == b.buttonLabel and o.bought == False:
                        price = o.cost
                        textSize(14)
                        fill(0, 0, 0)
                        text("$" + str(price) + ".00", xPos, yPos)
            elif b.buttonType == "mouseOverButton" and b.buttonOn:
                if b.buttonLabel == "Sponsor":
                    sponsorX = b.xPos - 30
                    sponsorY = b.yPos + 20
                    for sponsoritem in sponsorList:
                        s = sponsoritem
                        mood = s.moodThreshold - s.mood
                        textAlign(LEFT)
                        textSize(12)
                        fill(192, 177, 177)
                        if s.sponsoring:
                            text(str(s.name) + " - " + "Sponsored", sponsorX, sponsorY)
                        else:
                            if mood > 100:
                                text(str(s.name) + " - " + "Not Impressed", sponsorX, sponsorY)
                            elif mood > 30:
                                text(str(s.name) + " - " + "Neutral", sponsorX, sponsorY)
                            elif mood > 0:
                                text(str(s.name) + " - " + "Impressed", sponsorX, sponsorY)
                        sponsorY += 13
                elif b.buttonLabel == "Follower":
                    followerX = b.xPos - 30
                    followerY = b.yPos + 20
                    for playeritem in playerList:
                        p = playeritem
                        total = p.followerTotal
                        textAlign(LEFT)
                        textSize(12)
                        fill(192, 177, 177)
                        if total > 0:
                            text("Total Followers - " + str(total), followerX, followerY)
                            followerY += 13
                            text("Fitness Fans - " + str(int((float(p.fitFollower) / float(total)) * 100)) + "%", followerX, followerY)
                            followerY += 13
                            text("Hipsters - " + str(int((float(p.hipFollower) / float(total)) * 100)) + "%", followerX, followerY)
                            followerY += 13
                            text("Lifestyle Fans - " + str(int((float(p.lifeFollower) / float(total)) * 100)) + "%", followerX, followerY)
                            followerY += 13
                            text("Fashionistas - " + str(int((float(p.fashFollower) / float(total)) * 100)) + "%", followerX, followerY)
                        else:
                            text("No Followers", followerX, followerY) 
                elif b.buttonLabel == "TurnsLeft":
                     turnsX = b.xPos
                     turnsY = b.yPos + 13
                     for playeritem in playerList:
                         p = playeritem
                         fill(200, 200, 200)
                         textSize(12)
                         text("TURNS", turnsX, turnsY)                   
                    
        else:
            continue  


def buttonKill():
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonOn:
            b.buttonOn = False

def snapButtonBuild():
    buttonX = 0
    buttonY = 0
    snapLabel = "SNAP"
    buttonColour = color(200, 200, 200, 10)
    snapButton = button(buttonX, buttonY, 49, 49, buttonColour, snapLabel, 3, "snapButton")

def snapButtonDisplay(phoneX, phoneY):
    buttonX = phoneX + phone.width / 2
    buttonY = phoneY + 320
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "SNAP":
            b.xPos = buttonX
            b.yPos = buttonY
            b.buttonOn = True
            fill(200, 200, 200)
            ellipse(b.xPos, b.yPos, 49, 49)
            buttonColour = color(255, 255, 255)
            fill(buttonColour)
            ellipse(b.xPos, b.yPos, 31, 31)
            b.display()
                                                                            
def snapButton():
    sponsorCheck()
    audienceCheck()
    for modeobject in modeList:
        m = modeobject
        m.locationOn = False
        m.outfitOn = False
        m.handMode = False
        m.bedcafeMode = False
    for locationobject in locationList:
        l = locationobject
        l.locationOn = False
    for itemobject in itemList:
        i = itemobject
        if i.itemOn == True:
            i.bought = i.name in hardGoods
            i.tiredItem += 1
            i.itemOn = False
        elif i.itemOn == False:
            i.tiredItem = 0
    for playeritem in playerList:
        p = playeritem 
        p.turnsLeft -= 1
    println("ding")
    

def turnsLeftButtonBuild():
    #set up and display # of turns left
    buttonColour = color(200, 200, 200, 10)
    buttonX = 0
    buttonY = 0
    turnsLeftLabel = "TurnsLeft"
    turnsleftButton = button(buttonX, buttonY, 30, 16, buttonColour, turnsLeftLabel, 3, "mouseOverButton")
    
def turnsLeftButtonDisplay(phoneX, phoneY):
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "TurnsLeft":
            b.xPos = phoneX + 78
            b.yPos = phoneY + 322
            b.buttonOn = True
            b.display()
            for playeritem in playerList:
                p = playeritem
                fill(200, 200, 200)
                textSize(18)
                text(str(p.turnsLeft), b.xPos, b.yPos)
            
        
def handModeButtonBuild():
    #set up and display selfie button
    buttonColour = color(200, 200, 200, 5)
    buttonX = 0
    buttonY = 0
    handmodeLabel = "Handmode"
    handmodeButton = button(buttonX, buttonY, 18, 18, buttonColour, handmodeLabel, 3, "handmodeButton")
    
def handModeButtonDisplay(phoneX, phoneY):
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "Handmode":
            b.xPos = phoneX + 200
            b.yPos = phoneY + 320
            b.buttonOn = True
            b.display()
            image(selfie, b.xPos, b.yPos)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                        

def sponsorButtonBuild():
    #set up and display sponsor button for mouseOver
    buttonColour = color(200, 200, 200, 10)
    buttonX = 0
    buttonY = 0
    sponsorLabel = "Sponsor"
    sponsorButton = button(buttonX, buttonY, 80, 25, buttonColour, sponsorLabel, 3, "mouseOverButton")
    
def sponsorButtonDisplay(phoneX, phoneY):
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "Sponsor":
            b.xPos = phoneX + 501
            b.yPos = phoneY + 445
            b.buttonOn = True
            b.display()


def followerButtonBuild():
    #set up and display follower button for mouseOver
    buttonColour = color(200, 200, 200, 10)
    buttonX = 0
    buttonY = 0
    followerLabel = "Follower"
    followerButton = button(buttonX, buttonY, 80, 25, buttonColour, followerLabel, 3, "mouseOverButton")
    
def followerButtonDisplay(phoneX, phoneY):
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "Follower":
            b.xPos = phoneX + 630
            b.yPos = phoneY + 445
            b.buttonOn = True
            b.display()


def introMenuButtonBuild():
    # set up and display play and help buttons buttons
    buttonColour = color(200, 200, 200, 5)
    buttonX = 0
    buttonY = 0
    helpLabel = "HELP"
    helpButton = button(
        buttonX, buttonY, 76, 23, buttonColour, helpLabel, 1, "gameStateButton")

def introMenuButtonDisplay(phoneX, phoneY, gameState):
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "HELP" and gameState == 0:
            b.xPos = phoneX + phone.width / 2
            b.yPos = phoneY + 268
            b.buttonOn = True
            imageMode(CENTER)
            image(instructions, b.xPos, b.yPos)
            b.display()
        elif b.buttonLabel == "HELP" and gameState == 3:
            b.xPos = phoneX + 58
            b.yPos = phoneY + 63
            b.buttonOn = True
            b.buttonWidth = 30
            b.buttonHeight = 15
            b.display()
            text(str(b.buttonLabel), b.xPos, b.yPos)


def helpMenuButtonBuild():
    # set up and display play and help buttons buttons
    buttonColour = color(200, 200, 200, 5)
    buttonX = 0
    buttonY = 0
    playLabel = "PLAY"
    playButton = button(
        buttonX, buttonY, 220, 35, buttonColour, playLabel, 3, "gameStateButton")

def helpMenuButtonDisplay(phoneX, phoneY):
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "PLAY":
            b.xPos = width / 2
            b.yPos = height - 60
            b.buttonOn = True
            b.display()
        
            
def restartButtonBuild():
    # set up and display restart button
    buttonColour = color(200, 200, 200, 0)
    buttonX = 0
    buttonY = 0
    playLabel = "RESTART"
    restartButton = button(
        buttonX, buttonY, 220, 35, buttonColour, playLabel, 0, "gameOverButton")
    
def restartButtonDisplay():
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "RESTART":
            b.xPos = 260
            b.yPos = height - 125
            b.buttonOn = True
            b.display()

    
def continueButtonBuild():
    # set up and display restart button
    buttonColour = color(200, 200, 200, 0)
    buttonX = 0
    buttonY = 0
    continueLabel = "CONTINUE"
    restartButton = button(
        buttonX, buttonY, 220, 35, buttonColour, continueLabel, 3, "gameOverButton")
    
def continueButtonDisplay():
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonLabel == "CONTINUE":
            b.xPos = 530
            b.yPos = height - 125
            b.buttonOn = True
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
            b.buttonOn = True
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
    buttonY = phoneY + 333
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonType == "foodButton":
            b.xPos = buttonX
            b.yPos = buttonY
            b.buttonOn = True
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
    buttonY = phoneY + 252
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonType == "itemButton":
            b.xPos = buttonX
            b.yPos = buttonY
            b.buttonOn = True
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
        buttonX, buttonY, 43, 43, buttonColour, sneakersLabel, 3, "shoeButton")
    heelsButton = button(
        buttonX, buttonY, 43, 43, buttonColour, heelsLabel, 3, "shoeButton")
    
def outfitButtonDisplay(phoneX, phoneY):
    buttonX = phoneX + 350
    buttonY = phoneY + 171
    for buttonitem in buttonList:
        b = buttonitem
        if b.buttonType == "outfitButton" or b.buttonType == "shoeButton":
            b.xPos = buttonX
            b.yPos = buttonY
            b.buttonOn = True
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
    textY = phoneY + 45
    textSize(14)
    textAlign(LEFT, TOP)
    text("Location", textX, textY)
    textY += 81
    text("Outfit", textX, textY)
    textY += 81
    text("Items", textX, textY)
    textY += 81
    text("Food", textX, textY)
    
            

#ALL OF THE BUTTON THINGS ARE FINISHED        

def gameOverCheck():
    for playeritem in playerList:
        p = playeritem
        if p.turnsLeft == 0:
            global gameState
            gameState = 4 
    return(gameState)       

def gameStateControl(stateValue):
    if stateValue == 0:
        buttonKill()
        gameState = 0
        phoneX = width / 2 - phone.width / 2
        phoneY = 46
        phoneDraw(phoneX, phoneY)
        logoDraw(phoneX, phoneY)
        introMenuButtonDisplay(phoneX, phoneY, gameState)
        

    elif stateValue == 1:
        buttonKill()
        phoneX = 0
        phoneY = 0
        helpBoxDraw(phoneX, phoneY)
        #phoneDraw(phoneX, phoneY)
        helpMenuButtonDisplay(phoneX, phoneY)

    elif stateValue == 2:
        gameState = 3

    elif stateValue == 3:
        buttonKill()
        gameState = 3
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
        sponsorButtonDisplay(phoneX, phoneY)
        followerButtonDisplay(phoneX, phoneY)
        handModeButtonDisplay(phoneX, phoneY)
        turnsLeftButtonDisplay(phoneX, phoneY)
        introMenuButtonDisplay(phoneX, phoneY, gameState)
        buttonMouseOver()
        
        #draw game things and snaps
        moneyDisplay(phoneX, phoneY)
        locationDraw(phoneX, phoneY)
        handDraw(phoneX, phoneY)
        charfoodDraw(phoneX, phoneY)
        bedcafeDraw(phoneX, phoneY)
        itemDraw(phoneX, phoneY)
        thumbDraw(phoneX, phoneY)
        tmDraw(phoneX, phoneY)
        
        #gameover check
        gameOverCheck()

    elif stateValue == 4:
        buttonKill()
        phoneX = width / 2
        phoneY = height / 2
        gameOverDraw(phoneX, phoneY)
        restartButtonDisplay()
        continueButtonDisplay()

def mouseClicked():
    buttonHittest()

def keyPressed():
    if key == "E" or key == "e":
        global gameState
        gameState = 4
        return(gameState)
    elif key == "R" or key == "r":
        global gameState
        gameState = 0
        return(gameState)
    elif key == "C" or key == "c":
        for playeritem in playerList:
            p = playeritem
            p.moneyTotal += 1000    

def setup():
    size(800, 600)
    
    #mode load
    gameMode()
    
    #asset loads
    fontLoad()
    pngLoad()
    soundLoad()
    
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
    sponsorButtonBuild()
    followerButtonBuild()
    handModeButtonBuild()
    turnsLeftButtonBuild()
    restartButtonBuild()
    continueButtonBuild()



def draw():
    background(255, 255, 255)
    gameStateControl(gameState)