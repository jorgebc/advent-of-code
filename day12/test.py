import os
from day12 import calculateFewestStepsToBestSignal

testInputData = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
testExpectedResult = 31
result = calculateFewestStepsToBestSignal(testInputData)
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"


def getInputFromFile(path):
    file_path = os.path.join(os.getcwd(), path)
    # Open the file in read-only mode
    inputFile = open(file_path, "r")

    # Read the entire file content
    input = inputFile.read()

    # Close the file
    inputFile.close()

    return input


inputText = getInputFromFile("day11\\input.txt")
result = calculateFewestStepsToBestSignal(inputText)
print(f"Part 1 result: {result}")
