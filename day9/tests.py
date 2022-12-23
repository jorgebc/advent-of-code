import os
from day9 import (
    calculateMove,
    moveTail,
    calculateTailVisitedPositions,
    calculateTailVisitedPositionsV2,
)


def testCalculateMove(message, head, tail, expectedMove):
    move = calculateMove(head, tail)

    expectedX = expectedMove["x"]
    moveX = move["x"]
    assert moveX == expectedX, print(f"{message} with result x {moveX}")

    expectedY = expectedMove["y"]
    moveY = move["y"]
    assert moveY == expectedY, print(f"{message} with result y {moveY}")


# fmt: off
calculateMoveTestInputs = [ 
            ["touching right",
             {"x" : 3, "y" : 2,},
             {"x" : 2, "y" : 2,},
             {"x" : 0, "y" : 0,}],
            
            ["touching left",
             {"x" : 3, "y" : 2,},
             {"x" : 4, "y" : 2,},
             {"x" : 0, "y" : 0,}],
            
            ["touching up",
             {"x" : 2, "y" : 3,},
             {"x" : 2, "y" : 2,},
             {"x" : 0, "y" : 0,}],
            
            ["touching down",
             {"x" : 2, "y" : 3,},
             {"x" : 2, "y" : 4,},
             {"x" : 0, "y" : 0,}],
            
            ["move right",
             {"x" : 4, "y" : 4,},
             {"x" : 2, "y" : 4,},
             {"x" : 1, "y" : 0,}],
            
            ["move left",
             {"x" : 4, "y" : 4,},
             {"x" : 6, "y" : 4,},
             {"x" : -1, "y" : 0,}],
            
            ["move up",
             {"x" : 4, "y" : 6,},
             {"x" : 4, "y" : 4,},
             {"x" : 0, "y" : 1,}],
                        
            ["touching diagonal up right",
             {"x" : 2, "y" : 2,},
             {"x" : 3, "y" : 3,},
             {"x" : 0, "y" : 0,}],
            
            ["touching diagonal down right",
             {"x" : 2, "y" : 2,},
             {"x" : 3, "y" : 1,},
             {"x" : 0, "y" : 0,}],
            
            ["touching diagonal down left",
             {"x" : 2, "y" : 2,},
             {"x" : 1, "y" : 1,},
             {"x" : 0, "y" : 0,}],
            
            ["touching diagonal up left",
             {"x" : 2, "y" : 2,},
             {"x" : 1, "y" : 3,},
             {"x" : 0, "y" : 0,}],
            
            ["diagonal up right",
             {"x" : 2, "y" : 2,},
             {"x" : 0, "y" : 0,},
             {"x" : 1, "y" : 1,}],
            
            ["diagonal down right",
             {"x" : 2, "y" : 2,},
             {"x" : 1, "y" : 4,},
             {"x" : 1, "y" : -1,}],
            
            ["diagonal down left",
             {"x" : 2, "y" : 2,},
             {"x" : 3, "y" : 4,},
             {"x" : -1, "y" : -1,}],
            
            ["diagonal up left",
             {"x" : 3, "y" : 3,},
             {"x" : 4, "y" : 1,},
             {"x" : -1, "y" : 1,}],
            
            ["covered",
             {"x" : 3, "y" : 3,},
             {"x" : 3, "y" : 3,},
             {"x" : 0, "y" : 0,}],
        ]
# fmt: on

for testInput in calculateMoveTestInputs:
    message, head, tail, expectedMove = testInput
    testCalculateMove(message, head, tail, expectedMove)


def testMoveTail(head, tail, expectedTail):
    moveTail(head, tail, [])
    expectedX = expectedTail["x"]
    expectedY = expectedTail["y"]
    assert tail["x"] == expectedTail["x"], f"Tail x should be {expectedX}"
    assert tail["y"] == expectedTail["y"], f"Tail y should be {expectedY}"


# fmt: off
moveTailTestInputs = [
            [{	"x" : 3, "y" : 4,},{"x" : 2, "y" : 2,},{"x" : 3, "y" : 3,}],
            [{	"x" : 4, "y" : 3,},{"x" : 2, "y" : 2,},{"x" : 3, "y" : 3,}],
            [{	"x" : 4, "y" : 2,},{"x" : 2, "y" : 2,},{"x" : 3, "y" : 2,}],
            [{	"x" : 2, "y" : 2,},{"x" : 2, "y" : 4,},{"x" : 2, "y" : 3,}],
            [{	"x" : 2, "y" : 3,},{"x" : 4, "y" : 3,},{"x" : 3, "y" : 3,}],
        ]
# fmt: on

for testInput in moveTailTestInputs:
    head, tail, expectedTail = testInput
    # testMoveTail(head, tail, expectedTail)


testInput = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
testExpectedResult = 13
result = calculateTailVisitedPositions(testInput)
assert result == testExpectedResult, f"Result should be 13 but was {result}"


def getInputFromFile(path):
    file_path = os.path.join(os.getcwd(), path)
    # Open the file in read-only mode
    inputFile = open(file_path, "r")

    # Read the entire file content
    input = inputFile.read()

    # Close the file
    inputFile.close()

    return input


inputText = getInputFromFile("day9\\input.txt")
result = calculateTailVisitedPositions(inputText)
print(f"Part 1: {result}")

testExpectedResult = 1
result = calculateTailVisitedPositionsV2(testInput, 10)
assert result == testExpectedResult, f"Result should be 1 but was {result}"

result = calculateTailVisitedPositionsV2(inputText, 10)
print(f"Part 2: {result}")
