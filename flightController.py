import time
import threading

routes = []

sortedRoutes = []

#state: startCoords, endCoords, timeOfStart, actualCoords, length

for i in range(5):
    routes.append([])


while True:
    for i in range(5):
        for x in range(len(routes[i])):
            if abs(routes[i][x][3][0] - routes[i][x][1][0]) < 1 and abs(routes[i][x][3][1] - routes[i][x][1][1]) < 1 < 1:
                del routes[i][x]
            else:
                nowTime = time.time()
                flightTime = notTime - routes[i][x][2]
                flightDistance = flightTime * 60
                coefLen = double(flightDistance) / double(routes[i][x][4]
                routes[i][x][3][0] = routes[i][x][0][0] + (routes[i][x][1][0] - routes[i][x][0][0]) * coefLen
                routes[i][x][3][1] = routes[i][x][0][1] + (routes[i][x][1][1] - routes[i][x][0][1]) * coefLen
    sortedRoutes = sorted(routes, key = len)
                                                    
        
