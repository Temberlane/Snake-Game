############################################
#Name: Thomas
#Program Description: This is a Video Game
#Date: Nov 30
#
############################################

import random

playerx = 195
playery = 145
xspeed = 0
yspeed = 0
speedincr = 1

def setup():
    global back, itemx, itemy, powerupx, powerupy
    size(400,300)
    frameRate(30)
    noStroke()
    textAlign(CENTER)
    
    #TODO:
    #Change the background to an appropriate image of your choosing.
    #Make sure you can CLEARLY see the player item, as well as the 
    #red item and green item.
    
    back = loadImage("background.JPG")
    
    background(back)
    
    itemx = 300
    itemy = 60
    
    powerupx = 120
    powerupy = 220

def draw():
    global playerx, playery, xspeed, yspeed, back, itemx, itemy, powerupx, powerupy
    playerx += xspeed
    playery += yspeed
    fill(0x66004477)
    # rect(0,0, width,height)
    background(back)

    fill('#FFFFFF')
    rect(playerx, playery, 10, 10)
    
    if playerx > width:
        playerx = 0
    if playerx < 0:
        playerx = width
    if playery < 0:
        playery = height
    if playery > height:
        playery = 0
      
        
    fill(0, 255, 0)
    rect(powerupx, powerupy, 10, 10) 
     
    fill('#FF0000')
    rect(itemx, itemy, 10, 10) # red item
        
    if (playerx+10 >= itemx and playerx <= itemx+10       #checks if the right edge of the head is overlapping the left edge of the red item
        and playery+10 >= itemy and playery <= itemy+10): #checks if the left edge of the head is overlapping the right edge of the red item
        fill('#00FF00')
        text('hit!', 373,28)
        itemx = random.randint(0, 390)
        itemy = random.randint(0, 290)
        
        playerx = random.randint(0, 390)
        playery = random.randint(0, 290)
    
    if (playerx+10 >= powerupx and playerx <= powerupx+10 and playery+10 >= powerupy and playery <= powerupy+10): 
        fill('#00FF00')
        text('hit!', 373,28)
        powerupx = random.randint(0, 390)
        powerupy = random.randint(0, 290)
        
        speedChange()

    #TODO:
    #A red item has already been made for you. Make the red item disappear and transport the white item to a random spot when touched. (we want to avoid touching the red item)
    #Make a green item similarly to the red item already made for you. Make the green item disappear and apply power-up (increase speed) when touched. (we want to touch the green item)
    #When an item has been touched, it will appear at some random new location
    #NOTE: increasing and decreasing the speed may not happen in the draw() function
    
    

def speedChange():
    global speedx, speedy, speedincr
    speedincr += 1
    
def keyTyped():
    print(key)

def keyPressed():
    global xspeed, yspeed, speedincr
    
    #TODO:
    #Create an if-elif statement that will check for the keys: w, a, s, d
    #set xspeed and yspeed to 0, -4, and 4 accordingly to the direction the key is going 
    
    if (key == 's'):
        yspeed = 4 * speedincr
        xspeed = 0
    elif (key == 'a'):
        xspeed = -4 * speedincr
        yspeed = 0
    elif (key == 'w'):
        yspeed = -4 * speedincr
        xspeed = 0
    elif (key == 'd'):
        xspeed = 4 * speedincr
        yspeed = 0
    else:
        xspeed = 0
        yspeed = 0
        
    print(key)
    
    #TODO:
    #Create an if-elif statement that will check for the keys: UP, DOWN, LEFT, RIGHT
    #set xspeed and yspeed to 0, -4, and 4 accordingly to the direction the key is going 
    if (key == CODED):
        if (keyCode == DOWN):
            yspeed = 4 * speedincr
            xspeed = 0
        elif (keyCode == LEFT):
            xspeed = -4 * speedincr
            yspeed = 0
        elif (keyCode == UP):
            yspeed = -4 * speedincr
            xspeed = 0
        elif (keyCode == RIGHT):
            xspeed = 4 * speedincr
            yspeed = 0
        else:
            xspeed = 0
            yspeed = 0
    
    print(keyCode)
