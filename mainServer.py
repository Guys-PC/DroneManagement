import math

#Data struct: [x1, y1, x2, y2, startTime, vSpeed, hSpeed]
activeList = []


#Function checkForIntersect:

#Objective: check for intersect of two vectors/sections

#Params:
# (ax1, ay1) - coord of the start point of the first vector/section
# (ax2, ay2) - coord of the end point of the first vector/section
# (bx1, by1) - coord of the start point of the second vector/section
# (bx2, by2) - coord of the end point of the second vector/section

#Returns: result of check (True if intersects, False if not)

#Stage of work: In progress

def checkForIntersect(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    v1 = (bx2-bx1)*(ay1-by1)-(by2-by1)*(ax1-bx1)
    v2 = (bx2-bx1)*(ay2-by1)-(by2-by1)*(ax2-bx1)
    v3 = (ax2-ax1)*(by1-ay1)-(ay2-ay1)*(bx1-ax1)
    v4 = (ax2-ax1)*(by2-ay1)-(ay2-ay1)*(bx2-ax1)
    if not v1*v1 < 0 or not v3*v4<0:
        return False
    else
        return True

#Function addNewRoute

#Objective: and a new route mission to the main database

#Params:
# (x1, y1) - coords of the start point of the route
# (x2, y2) - coords of the end point of the route

#Returns: nothing

#Stage of work: In progress

def addNewRoute(x1, y1, x2, y2):
    global activeList
    found = False
    for i in range(5):
        for x in activeList[i]:
            if not checkForIntersect

#Start of the main process

#Init five vertical layers of the 3d route map
for i in range(5):
    activeList.append([])

