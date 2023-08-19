import Globals as g
import random
import math

def initScreen(minX, maxX, minY, maxY):
    g.minX = minX
    g.maxX = maxX
    g.minY = minY
    g.maxY = maxY

def setPlayerPosition(x, y):
    g.playerX = x
    g.playerY = y

def setGoal():
    isExist = True
    while isExist :
        randX = random.randint(g.minX, g.maxY)
        randY = random.randint(g.minY, g.maxY)
        if randX != g.playerX and randY != g.playerY :
            g.goalX = randX
            g.goalY = randY
            isExist = False

def spawnEnemies(level):
    if level == "MEDIUM" : g.countEnemies = 10
    elif level == "HARD" : g.countEnemies = 100

    for i in range(g.countEnemies):
        isExist = True
        while isExist :
            randX = random.randint(g.minX, g.maxY)
            randY = random.randint(g.minY, g.maxY)
            if randX != g.playerX and randY != g.playerY and randX != g.goalX and randY != g.goalY :
                g.enemiesX.append(randX)
                g.enemiesY.append(randY)
                isExist = False

# def lenEnemies():
# return len(g.countEnemies)

def displayInitStats(level):
    print("Posisi player sekarang     : " + str(g.playerX) + " " + str(g.playerY))
    print("Banyaknya musuh : " + str(g.countEnemies))

def distanceEuclid(x1, y1, x2, y2):
    x = (x1, y1, 0)
    y = (x2, y2, 0)
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance

def distancePlayerwithGoal():
    return distanceEuclid(g.playerX, g.playerY, g.goalX, g.goalY)

def displayInGameStats():
    print("jarak antara player dengan bintang : " + str(distancePlayerwithGoal()))

def checkPlayerMove(move):
    if move == "UP" : g.playerY += 1
    elif move == "DOWN" : g.playerY -= 1
    elif move == "LEFT" : g.playerX -= 1
    elif move == "RIGHT" : g.playerX += 1

    if g.playerX < g.minX or g.playerX > g.maxX or g.playerY < g.minY or g.playerY > g.maxY :
        print("GAME OVER!")
        return False

    isNabrak = False
    for i in range(g.countEnemies) :
        if g.playerX == g.enemiesX[i] and g.playerY == g.enemiesY[i] :
           isNabrak = True
           break
    if isNabrak :
        print("GAME OVER!") 
        return False

    if g.playerX == g.goalX and g.playerY == g.goalY :
        print("YOU WIN!")
        return False

    displayInGameStats()