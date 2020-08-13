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
    isIntersecting = 1
    xCross, yCross = 0, 0
    k1, b1 = getCoef(ax1, ay1, ax2, ay2)
    k2, b2 = getCoef(bx1, by1, bx2, by2)
    if k1 == k2:
        if b1 == b2:
            isIntersecting = 2
        else:
            isIntersecting = 1
    else:
        isIntersecting = 0
        if b1 == b2:
            xCross, yCross = 0, b1
        else:
            xCross = (b2 - b1) / (k1 - k2)
            yCross = k1 * xCross + b1
    return isIntersecting, xCross, yCross
    
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
               isCrossing, x, y = checkForIntersect(x1New, y1New, x2New, y2New, r[0][0], r[0][1], r[1][0], r[1][1])
               if isCrossing == 0:
                   anyCrossing = True
                   print("failed")
                   break
            if anyCrossing == 1 or anyCrossing == 2:
                wasPassed = True
                print("passed")
                chosenLevel = i
                break
    routes[chosenLevel].append([[x1New, y1New], [x2New, y2New], time.time(), sqrt(sqr(x2New - x1New) + sqr(y2New - y1New))])
    print("Added new route on " + str(chosenLevel))
    
    """fig = plt.figure()
    
    ax1New = random.randint(0, 100)
    ay1New = random.randint(0, 100)

    ax2New = random.randint(0, 100)
    ay2New = random.randint(0, 100)
    
    bx1New = random.randint(0, 100)
    by1New = random.randint(0, 100)

    bx2New = random.randint(0, 100)
    by2New = random.randint(0, 100)
    
    isCrossing, x, y = checkForIntersect(ax1New, ay1New, ax2New, ay2New, bx1New, by1New, bx2New, by2New)
    
    graph1 = plt.plot([ax1New, ay1New], [ax2New, ay2New])
    graph2 = plt.plot([bx1New, by1New], [bx2New, by2New])
    
    if isCrossing == 0:
        print("true")
    else:
        print("false")
    
    plt.show()"""
    
