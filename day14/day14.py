def parseLinesCoords(data):
    lines = data.split("\n")
    linesCoords = []
    for line in lines:
        coordsString = line.split(" -> ")

        newLineCoord = []
        for coordString in coordsString:
            pointString = coordString.split(",")
            linePoint = [int(pointString[0]), int(pointString[1])]
            newLineCoord.append(linePoint)

        linesCoords.append(newLineCoord)

    return linesCoords


def getMapSize(linesCoords):

    height = 0
    minWidth = 9999999999
    maxWidth = 0

    for lineCoord in linesCoords:
        for coord in lineCoord:

            if coord[0] > maxWidth:
                maxWidth = coord[0]
            if coord[0] < minWidth:
                minWidth = coord[0]

            if coord[1] > height:
                height = coord[1]

    return [height, maxWidth, minWidth]


def drawPoint(coords, widthCorrection, mapArray):
    row = coords[1]
    col = coords[0] - widthCorrection
    mapArray[row][col] = "#"


def drawLine(fr0m, to, mapArray):
    return 0


def updateMap(mapArray, widthCorrection, lineCoords):
    if len(lineCoords) == 1:
        drawPoint(lineCoords[0], widthCorrection, mapArray)
        return

    else:
        fr0m = lineCoords[0]
        to = lineCoords[1]
        drawLine(fr0m, to, mapArray)
        return updateMap(mapArray, widthCorrection, lineCoords[1:])


def parseMap(linesCoords, height, maxWidth, minWidth):
    totalWidth = maxWidth - minWidth + 1
    totalHeight = height + 1
    mapArray = [["."] * totalWidth] * totalHeight

    for lineCoords in linesCoords:
        print(lineCoords)
        updateMap(mapArray, minWidth, lineCoords)

    return mapArray


def createMapData(data):
    linesCoords = parseLinesCoords(data)
    height, maxWidth, minWidth = getMapSize(linesCoords)
    mAp = parseMap(linesCoords, height, maxWidth, minWidth)

    return {"map": mAp, "height": height, "maxWidth": maxWidth, "minWidth": minWidth}
