import string
from treelib import Tree

alphabet = list(string.ascii_lowercase)


def split(word):
    return list(word)


def getHeightValue(height):
    return alphabet.index(height) + 1


def parseHeightMap(inputMap):

    mapLines = inputMap.split("\n")

    mapRows = len(mapLines)
    mapCols = len(mapLines[0])

    heightMap = {
        "map": [],
        "startingPosition": [],
        "bestSignalPosition": [],
        "mapRows": mapRows,
        "mapCols": mapCols,
    }

    for row in range(mapRows):
        newRow = [0] * mapCols
        heightMap["map"].append(newRow)

        for col in range(mapCols):
            height = mapLines[row][col]
            if height == "S":
                heightMap["startingPosition"] = [row, col]
                heightMap["map"][row][col] = getHeightValue("a")
            elif height == "E":
                heightMap["bestSignalPosition"] = [row, col]
                heightMap["map"][row][col] = getHeightValue("z")
            else:
                heightMap["map"][row][col] = getHeightValue(height)

    return heightMap


def printHeightMap(heightMap):
    print(f"Starting position: {heightMap['startingPosition']}")
    print(f"Best signal position: {heightMap['bestSignalPosition']}")
    print(f"Map rows: {heightMap['mapRows']}")
    print(f"Map cols: {heightMap['mapCols']}")
    for row in heightMap["map"]:
        print(row)


def createIdentifier(row, col):
    return f"[{row},{col}]"


def isBestSignalPosition(position, heightMap):
    return position == heightMap["bestSignalPosition"]


def positionHasBeenVisited(paths, position, parent):
    mirar el identifier del padre que son todos los ids de los padres concatenados
    parents = paths.rsearch(parent)
    print(len(parents))
    for p in parents:
        print(p)
    print(parents)


def createPaths(paths, parent, lastPosition, heightMap):

    if positionHasBeenVisited(paths, lastPosition, parent):
        return

    actualPosition = [0, 0]
    if isBestSignalPosition(actualPosition, heightMap):
        tag = ",".join(actualPosition)
        identifier = parent.identifier + createIdentifier(*actualPosition)
        return paths.create_node(tag, identifier, parent)

    actualRox, actualCol = actualPosition
    return


def calculateFewestStepsToBestSignal(inputMap):
    heightMap = parseHeightMap(inputMap)
    printHeightMap(heightMap)

    paths = Tree()
    startIdentifier = createIdentifier(*heightMap["startingPosition"])
    paths.create_node("S", startIdentifier)

    createPaths(
        paths, paths.get_node(startIdentifier), heightMap["startingPosition"], heightMap
    )

    paths.show()

    return 0
