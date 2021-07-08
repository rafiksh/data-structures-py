def spiral_index(y, x):
    directionArray = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    directionIndex = 0
    movementStep = 1
    currentPoint = (0, 0)
    value = 0
    while currentPoint != (x, y):
        for i in range(movementStep):
            if currentPoint != (x, y):
                currentPoint = (currentPoint[0] + directionArray[directionIndex % 4][0],
                                currentPoint[1] + directionArray[directionIndex % 4][1])
                value += 1

        directionIndex += 1

        for i in range(movementStep):
            if currentPoint != (x, y):
                currentPoint = (currentPoint[0] + directionArray[directionIndex % 4][0],
                                currentPoint[1] + directionArray[directionIndex % 4][1])
                value += 1

        directionIndex += 1
        movementStep += 1
    print("Spiral index of (%s, %s) is %s." % (y, x, value))


if __name__ == '__main__':
    spiral_index(1000, 1000)
