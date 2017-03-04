def phoneLoad():
    global phone 
    phone = loadImage("Phone.png")

def phoneDraw():
    global phone
    phoneWidth = 417
    phoneHeight = 872
    imageMode(CENTER)
    pushMatrix()
    scale(2)
    image(phone, width/4, height/4)
    popMatrix()
    
class button(object): #class defenition
    def __init__(self, yPos, xPos, strokeColour):  #object instructor
        self.yPos = yPos 
        self.xPos = xPos
        self.strokeColour = strokeColour
        
    def display(self): #display method
        noFill()
        rectMode(CENTER)
        stroke(self.strokeColour)
        
        

def setup():
    size(800, 600)
    phoneLoad()

def draw():
    background(255, 255, 255)
    shapeMode(CENTER)
    phoneDraw()

