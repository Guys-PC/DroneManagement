import time
import threading
import random
from math import *
import matplotlib.pyplot as plt

def sqr(a):
    return a * a

def getCoef(x1, y1, x2, y2):
    if y2 > y1:
        y1, y2 = y2, y1
        x1, x2 = x2, x1
    yDiff = y2 - y1
    xDiff = x2 - x1
    k = yDiff / xDiff
    b = y1 - k * x1
    return k, b
    

def checkForIntersect(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    """v1 = (bx2-bx1)*(ay1-by1)-(by2-by1)*(ax1-bx1)
    v2 = (bx2-bx1)*(ay2-by1)-(by2-by1)*(ax2-bx1)
    v3 = (ax2-ax1)*(by1-ay1)-(ay2-ay1)*(bx1-ax1)
    v4 = (ax2-ax1)*(by2-ay1)-(ay2-ay1)*(bx2-ax1)
    if not v1*v1 < 0 or not v3*v4<0:
        return False
    else:
        return True"""
    print("1")

#[[xStart, yStart], [xEnd, yEnd], startTime, length]

def getCoords(inp):
    nowTime = time.time()
    flightTime = nowTime - inp[2]
    flightDistance = flightTime * 60
    coefLen = double(flightDistance) / double(inp[3])
    xNow = inp[0][0] + (inp[1][0] - inp[0][0]) * coefLen
    yNow = inp[0][1] + (inp[1][1] - inp[0][1]) * coefLen


routes = []

sortedRoutes = []

#state: startCoords, endCoords, timeOfStart, length

for i in range(5):
    routes.append([])


for i in range(50):
    ##### Update state of active routes #####

    ##### ----- #####

    ##### Add new route #####
    
    x1New = random.randint(0, 10)
    y1New = random.randint(0, 10)

    x2New = random.randint(0, 10)
    y2New = random.randint(0, 10)

    wasPassed = False
    chosenLevel = -1

    while not wasPassed:
        for i in range(5):
            anyCrossing = False
            for r in routes[i]:
               isCrossing = checkForIntersect(x1New, y1New, x2New, y2New, r[0][0], r[0][1], r[1][0], r[1][1])
               if isCrossing == True:
                   anyCrossing = True
                   print("failed")
                   break
            if anyCrossing == False:
                wasPassed = True
                print("passed")
                chosenLevel = i
                break
    routes[chosenLevel].append([[x1New, y1New], [x2New, y2New], time.time(), sqrt(sqr(x2New - x1New) + sqr(y2New - y1New))])
    print("Added new route on " + str(chosenLevel))


                                                          
        
