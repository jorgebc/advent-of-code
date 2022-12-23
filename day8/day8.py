import os

# Part 1

testInput = """30373
25512
65332
33549
35390"""


def parseMatrix(input):
    matrix = []

    lines = input.split("\n")
    for line in lines:
        row = []
        for value in line:
            row.append(int(value))

        matrix.append(row)

    return matrix


parseMatrixTestResult = parseMatrix(testInput)
upperLeft = 3
assert (
    parseMatrixTestResult[0][0] == upperLeft
), f"Upper left should be {str(upperLeft)}, but was {upperLeft}"
lowerRight = 0
assert (
    parseMatrixTestResult[4][4] == lowerRight
), f"Lower right should be {str(upperLeft)}, but was {lowerRight}"


def getGridLengths(grid):
    colLength = len(grid)
    rowLength = len(grid[0])
    return [colLength, rowLength]


def isEdgeTree(row, col, grid):
    colLength, rowLength = getGridLengths(grid)
    if col == 0 or col == colLength:
        return True
    elif row == 0 or row == rowLength:
        return True
    else:
        return False


is00Edge = isEdgeTree(0, 0, parseMatrixTestResult)
assert is00Edge == True, "0 0 should be edge"
is11Edge = isEdgeTree(0, 0, parseMatrixTestResult)
assert is11Edge == True, "1 1 should be edge"
is44Edge = isEdgeTree(5, 5, parseMatrixTestResult)
assert is44Edge == True, "5 5 should be edge"
is23Edge = isEdgeTree(2, 3, parseMatrixTestResult)
assert is23Edge == False, "2 3 should no be edge"


def isVisible(row, col, start, stop, grid, isCol):
    treeHeight = grid[row][col]
    for num in range(start, stop):
        if isCol and treeHeight <= grid[row][num]:
            return False
        if not isCol and treeHeight <= grid[num][col]:
            return False

    return True


def isVisibleFromNorth(row, col, grid):
    return isVisible(row, col, 0, row, grid, False)


is11VisibleFromNorth = isVisibleFromNorth(1, 1, parseMatrixTestResult)
assert is11VisibleFromNorth == True, "1 1 should be visible from north"
is21VisibleFromNorth = isVisibleFromNorth(2, 1, parseMatrixTestResult)
assert is21VisibleFromNorth == False, "2 1 should not be visible from north"
is43VisibleFromNorth = isVisibleFromNorth(4, 3, parseMatrixTestResult)
assert is43VisibleFromNorth == True, "4 3 should be visible from north"


def isVisibleFromEast(row, col, grid):
    return isVisible(row, col, col + 1, len(grid[col]), grid, True)


is11VisibleFromEast = isVisibleFromEast(1, 1, parseMatrixTestResult)
assert is11VisibleFromEast == False, "1 1 should not be visible from east"
is21VisibleFromEast = isVisibleFromEast(2, 1, parseMatrixTestResult)
assert is21VisibleFromEast == True, "2 1 should be visible from east"


def isVisibleFromSouth(row, col, grid):
    return isVisible(row, col, row + 1, len(grid), grid, False)


is11VisibleFromSouth = isVisibleFromSouth(1, 1, parseMatrixTestResult)
assert is11VisibleFromSouth == False, "1 1 should not be visible from south"
is21VisibleFromSouth = isVisibleFromSouth(2, 1, parseMatrixTestResult)
assert is21VisibleFromSouth == False, "2 1 should not be visible from south"
is32VisibleFromSouth = isVisibleFromSouth(3, 2, parseMatrixTestResult)
assert is32VisibleFromSouth == True, "3 2 should be visible from south"


def isVisibleFromWest(row, col, grid):
    return isVisible(row, col, 0, col, grid, True)


is11VisibleFromWest = isVisibleFromWest(1, 1, parseMatrixTestResult)
assert is11VisibleFromWest == True, "1 1 should be visible from West"
is21VisibleFromWest = isVisibleFromWest(2, 1, parseMatrixTestResult)
assert is21VisibleFromWest == False, "2 1 should not be visible from West"
is32VisibleFromWest = isVisibleFromWest(3, 2, parseMatrixTestResult)
assert is32VisibleFromWest == True, "3 2 should be visible from West"


def isInteriorTreeVisible(row, col, grid):
    return (
        isVisibleFromNorth(row, col, grid)
        or isVisibleFromEast(row, col, grid)
        or isVisibleFromSouth(row, col, grid)
        or isVisibleFromWest(row, col, grid)
    )


is11Visible = isInteriorTreeVisible(1, 1, parseMatrixTestResult)
assert is11Visible == True, "1 1 should be visible"


def isTreeVisible(row, col, grid):
    return isEdgeTree(col, row, grid) or isInteriorTreeVisible(row, col, grid)


is00Visible = isTreeVisible(0, 0, parseMatrixTestResult)
assert is00Visible == True, "0 0 should be visible"
is11Visible = isTreeVisible(1, 1, parseMatrixTestResult)
assert is11Visible == True, "1 1 should be visible"
is44Visible = isTreeVisible(4, 4, parseMatrixTestResult)
assert is44Visible == True, "4 4 should be visible"
is23Visible = isTreeVisible(2, 3, parseMatrixTestResult)
assert is23Visible == True, "2 3 should be visible"
is22Visible = isTreeVisible(2, 2, parseMatrixTestResult)
assert is22Visible == False, "2 2 should not be visible"


def countVisibleTreesFromOutside(input):

    treeGrid = parseMatrix(input)
    colLength, rowLength = getGridLengths(treeGrid)

    visibleTrees = 0

    for row in range(rowLength):
        for col in range(colLength):
            if isTreeVisible(row, col, treeGrid):
                visibleTrees += 1

    return visibleTrees


expectedResult = 21
testResult = countVisibleTreesFromOutside(testInput)
assert (
    testResult == expectedResult
), f"Result should be {str(expectedResult)}, but was {testResult}"


def getInputFromFile():
    file_path = os.path.join(os.getcwd(), "day8\\input.txt")
    # Open the file in read-only mode
    inputFile = open(file_path, "r")

    # Read the entire file content
    input = inputFile.read()

    # Close the file
    inputFile.close()

    return input


input = getInputFromFile()
part1Result = countVisibleTreesFromOutside(input)
print(f"Part 1 result is: {part1Result}")

# Part 2


def calculateViewingDistance(row, col, start, stop, grid, isCol, isBackwards):
    scenicScore = 0

    if isEdgeTree(row, col, grid):
        return scenicScore

    sequence = range(start, stop)
    if isBackwards:
        sequence = list(reversed(sequence))

    treeHeight = grid[row][col]
    for num in sequence:
        scenicScore += 1
        if isCol and treeHeight <= grid[row][num]:
            break
        if not isCol and treeHeight <= grid[num][col]:
            break

    return scenicScore


def calculateNorthViewingDistance(row, col, grid):
    return calculateViewingDistance(row, col, 0, row, grid, False, True)


testResult = calculateNorthViewingDistance(0, 0, parseMatrixTestResult)
assert testResult == 0, f"0 0 should score north 0, but was {testResult}"
testResult = calculateNorthViewingDistance(1, 2, parseMatrixTestResult)
assert testResult == 1, f"1 2 should score north 1, but was {testResult}"
testResult = calculateNorthViewingDistance(3, 2, parseMatrixTestResult)
assert testResult == 2, f"3 2 should score north 2, but was {testResult}"
testResult = calculateNorthViewingDistance(3, 3, parseMatrixTestResult)
assert testResult == 3, f"3 3 should score north 3, but was {testResult}"


def calculateEastViewingDistance(row, col, grid):
    return calculateViewingDistance(
        row, col, col + 1, len(grid[col]), grid, True, False
    )


testResult = calculateEastViewingDistance(3, 2, parseMatrixTestResult)
assert testResult == 2, f"3 2 should score east 2, but was {testResult}"
testResult = calculateEastViewingDistance(1, 2, parseMatrixTestResult)
assert testResult == 2, f"1 2 should score east 2, but was {testResult}"


def calculateSouthViewingDistance(row, col, grid):
    return calculateViewingDistance(row, col, row + 1, len(grid), grid, False, False)


testResult = calculateSouthViewingDistance(3, 2, parseMatrixTestResult)
assert testResult == 1, f"3 2 should score south 1, but was {testResult}"
testResult = calculateSouthViewingDistance(1, 2, parseMatrixTestResult)
assert testResult == 2, f"1 2 should score south 2, but was {testResult}"


def calculateWestViewingDistance(row, col, grid):
    return calculateViewingDistance(row, col, 0, col, grid, True, True)


testResult = calculateWestViewingDistance(3, 2, parseMatrixTestResult)
assert testResult == 2, f"3 2 should score west 2, but was {testResult}"
testResult = calculateWestViewingDistance(1, 2, parseMatrixTestResult)
assert testResult == 1, f"1 2 should score west 1, but was {testResult}"


def calculateScenicScore(row, col, grid):
    northViewingDistance = calculateNorthViewingDistance(row, col, grid)
    eastViewingDistance = calculateEastViewingDistance(row, col, grid)
    southViewingDistance = calculateSouthViewingDistance(row, col, grid)
    westViewingDistance = calculateWestViewingDistance(row, col, grid)
    return (
        northViewingDistance
        * eastViewingDistance
        * southViewingDistance
        * westViewingDistance
    )


testResult = calculateScenicScore(3, 2, parseMatrixTestResult)
assert testResult == 8, f"3 2 should score 8, but was {testResult}"
testResult = calculateScenicScore(1, 2, parseMatrixTestResult)
assert testResult == 4, f"1 2 should score 4, but was {testResult}"


def getHighestScenicScore(grid):

    highestScenicScore = 0
    for rows in grid:
        for scenicScore in rows:
            if scenicScore > highestScenicScore:
                highestScenicScore = scenicScore

    return highestScenicScore


def getHighestScenicScoreTree(input):

    treeGrid = parseMatrix(input)
    colLength, rowLength = getGridLengths(treeGrid)

    scenicScoreGrid = [[0] * rowLength for _ in range(colLength)]

    for row in range(rowLength):
        for col in range(colLength):
            scenicScore = calculateScenicScore(row, col, treeGrid)
            scenicScoreGrid[row][col] = scenicScore

    highestScenicScore = getHighestScenicScore(scenicScoreGrid)

    return highestScenicScore


expectedResult = 8
testResult = getHighestScenicScoreTree(testInput)
assert (
    testResult == expectedResult
), f"Result should be {str(expectedResult)}, but was {testResult}"

part2Result = getHighestScenicScoreTree(input)
print(f"Part 2 result is: {part2Result}")
