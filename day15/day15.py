def extractCoords(data, splitString):
    beacon = data.split(splitString)[1].split(", ")
    x = int(beacon[0].split("=")[1])
    y = int(beacon[1].split("=")[1])

    return {"x": x, "y": y}


def calculateDistances(sensorCoords, beaconCoords):
    xDistance = sensorCoords["x"] - beaconCoords["x"]
    yDistance = sensorCoords["y"] - beaconCoords["y"]
    return {
        "xDistance": xDistance,
        "yDistance": yDistance,
        "distance": abs(xDistance) + abs(yDistance),
    }


def extractSensorBeacon(line):
    sensorData, beaconData = line.split(": closest ")
    sensorCoords = extractCoords(sensorData, "Sensor at ")
    beaconCoords = extractCoords(beaconData, "beacon is at ")

    distances = calculateDistances(sensorCoords, beaconCoords)

    return {
        "sensorCoords": sensorCoords,
        "beaconCoords": beaconCoords,
        "distances": distances,
    }


def maxCorrection(coord, distance, actualCorrection):
    possibleCorrection = coord - distance
    if actualCorrection > possibleCorrection:
        return possibleCorrection
    else:
        return actualCorrection


def extractCorrections(sensorsBeacons):
    xCorrection = 0
    yCorrection = 0
    for sensorBeacon in sensorsBeacons:
        distance = sensorBeacon["distances"]["distance"]
        xCoord = sensorBeacon["sensorCoords"]["x"]
        yCoord = sensorBeacon["sensorCoords"]["y"]
        xCorrection = maxCorrection(xCoord, distance, xCorrection)
        yCorrection = maxCorrection(yCoord, distance, yCorrection)

    return [abs(xCorrection), abs(yCorrection)]


def printSensorsBeaconsData(sensorsBeaconsData):
    for item in sensorsBeaconsData["sensorsBeacons"]:
        print(item)

    print(f"xCorrection: {sensorsBeaconsData['xCorrection']}")
    print(f"yCorrection: {sensorsBeaconsData['yCorrection']}")


def parseSensorBeaconData(data):

    sensorsBeaconsData = {"sensorsBeacons": [], "xCorrection": 0, "yCorrection": 0}
    lines = data.split("\n")

    for line in lines:
        sensorBeacon = extractSensorBeacon(line)
        sensorsBeaconsData["sensorsBeacons"].append(sensorBeacon)

    xCorrection, yCorrection = extractCorrections(sensorsBeaconsData["sensorsBeacons"])
    sensorsBeaconsData["xCorrection"] = xCorrection
    sensorsBeaconsData["yCorrection"] = yCorrection

    printSensorsBeaconsData(sensorsBeaconsData)
    return sensorsBeaconsData


def calculateMapSize(sensorsBeaconsData):
    height = 0
    width = 0

    xCorrection = sensorsBeaconsData["xCorrection"]
    yCorrection = sensorsBeaconsData["yCorrection"]

    for sensorBeacon in sensorsBeaconsData["sensorsBeacons"]:
        xCoord = sensorBeacon["sensorCoords"]["x"]
        yCoord = sensorBeacon["sensorCoords"]["y"]

        possibleWidth = xCoord + xCorrection
        possibleHeight = yCoord + yCorrection

        if possibleHeight > height:
            height = possibleHeight
        if possibleWidth > width:
            width = possibleWidth

    return [height + 10, width + 10]


def printSensorBeaconMap(sensorBeaconMap):
    i = -1
    for row in sensorBeaconMap:
        i += 1
        print(str(i) + " " + "".join(row))


def addSignal(sensorRow, row, sensorCol, col, sensorBeaconMap, distance):
    if abs(row) + abs(col) > distance:
        return
    if (
        sensorBeaconMap[sensorRow + row][sensorCol + col] != "S"
        and sensorBeaconMap[sensorRow + row][sensorCol + col] != "B"
    ):
        sensorBeaconMap[sensorRow + row][sensorCol + col] = "#"


def createMap(width, height):
    sensorBeaconMap = []

    print("Creating map")
    for row in range(height):
        newRow = []
        for col in range(width):
            newRow.append(".")

        sensorBeaconMap.append(newRow)

    return sensorBeaconMap


def createSensorBeaconMap(sensorsBeaconsData):

    height, width = calculateMapSize(sensorsBeaconsData)
    print(f"heigh: {height}")
    print(f"width: {width}")

    sensorBeaconMap = createMap(width, height)

    xCorrection = sensorsBeaconsData["xCorrection"]
    yCorrection = sensorsBeaconsData["yCorrection"]

    print("Filling map")
    for sensorBeacon in sensorsBeaconsData["sensorsBeacons"]:

        distance = sensorBeacon["distances"]["distance"]
        sensorRow = sensorBeacon["sensorCoords"]["y"] + yCorrection
        sensorCol = sensorBeacon["sensorCoords"]["x"] + xCorrection
        beaconRow = sensorBeacon["beaconCoords"]["y"] + yCorrection
        beaconCol = sensorBeacon["beaconCoords"]["x"] + xCorrection

        sensorBeaconMap[sensorRow][sensorCol] = "S"
        sensorBeaconMap[beaconRow][beaconCol] = "B"

        for x in range(distance + 1):
            for y in range(distance + 1):

                addSignal(sensorRow, x, sensorCol, y, sensorBeaconMap, distance)
                addSignal(sensorRow, x, sensorCol, -y, sensorBeaconMap, distance)
                addSignal(sensorRow, -x, sensorCol, y, sensorBeaconMap, distance)
                addSignal(sensorRow, -x, sensorCol, -y, sensorBeaconMap, distance)

    printSensorBeaconMap(sensorBeaconMap)
    return sensorBeaconMap


def calculateRowPositionsCannotContainBeaconWithMap(rowNum, data):
    sensorsBeaconsData = parseSensorBeaconData(data)
    sensorBeaconMap = createSensorBeaconMap(sensorsBeaconsData)

    positions = 0
    correction = sensorsBeaconsData["yCorrection"]
    row = sensorBeaconMap[rowNum + correction]
    print("Calculating")
    for item in row:
        if item == "#":
            positions += 1

    return positions


def addPosition(row, col, rowNum, positions):
    if row == rowNum:
        positions.append(str(row) + str(col))


def calculate(rowNum, sensorsBeaconsData):

    # height, width = calculateMapSize(sensorsBeaconsData)
    # print(f"heigh: {height}")
    # print(f"width: {width}")

    xCorrection = sensorsBeaconsData["xCorrection"]
    yCorrection = sensorsBeaconsData["yCorrection"]
    ##rowNum += yCorrection
    occupiedPositions = []

    positions = []
    for sensorBeacon in sensorsBeaconsData["sensorsBeacons"]:

        distance = sensorBeacon["distances"]["distance"]
        sensorRow = sensorBeacon["sensorCoords"]["y"]
        sensorCol = sensorBeacon["sensorCoords"]["x"]
        beaconRow = sensorBeacon["beaconCoords"]["y"]
        beaconCol = sensorBeacon["beaconCoords"]["x"]

        if sensorRow == rowNum:
            occupiedPositions.append(str(sensorRow) + str(sensorCol))

        if beaconRow == rowNum:
            occupiedPositions.append(str(beaconRow) + str(beaconCol))

        for x in range(distance + 1):
            if sensorRow + x == rowNum or sensorRow - x == rowNum:
                for y in range(distance + 1):

                    if abs(x) + abs(y) <= distance:
                        row = sensorRow + x
                        col = sensorCol + y
                        addPosition(row, col, rowNum, positions)

                        row = sensorRow - x
                        col = sensorCol + y
                        addPosition(row, col, rowNum, positions)

                        row = sensorRow + x
                        col = sensorCol - y
                        addPosition(row, col, rowNum, positions)

                        row = sensorRow - x
                        col = sensorCol - y
                        addPosition(row, col, rowNum, positions)

    positions.sort()
    positionsSet = set(positions)
    occupiedPositionsSet = set(occupiedPositions)
    # print(f"Signal positions {positionsSet}")
    # print(f"Positions occupied {occupiedPositionsSet}")
    return len(positionsSet) - len(occupiedPositionsSet)


def calculateRowPositionsCannotContainBeacon(rowNum, data):
    sensorsBeaconsData = parseSensorBeaconData(data)
    return calculate(rowNum, sensorsBeaconsData)


"10-2"
"10-1"
"100"
"101"
"102"
"103"
"104"
"105"
"106"
"107"
"108"
"109"
"1010"
"1011"
"1012"
"1013"
"1014"
"1015"
"1016"
"1017"
"1018"
"1019"
"1020"
"1021"
"1022"
"1023"
"1024"
