import os
from day25 import translateNumberToDecimal, translateNumbersToDecimal, fromDecimalToBase,decimalToSanafu, fixMultiDigit

testExpectedResult = ["1-"]
result = fixMultiDigit(["1-"])
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"

testExpectedResult = ["2","-"]
result = fixMultiDigit(["1", "1-"])
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"



testExpectedResult = 1
result = translateNumberToDecimal("1")
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"

testExpectedResult = 3
result = translateNumberToDecimal("1=")
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"

testExpectedResult = 2022
result = translateNumberToDecimal("1=11-2")
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"

testData = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

testExpectedResult = [1747, 906, 198, 11, 201, 31, 1257, 32, 353, 107, 7, 3, 37]
result = translateNumbersToDecimal(testData)
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"
print(f"Part 1 test: {sum(result)}")

testExpectedResult = ["2", "=", "-", "1", "=", "0"]
result = decimalToSanafu(sum(result))
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


inputText = getInputFromFile("day25\\input.txt")
result = translateNumbersToDecimal(inputText)
print(result)
print(f"Sum del result: {sum(result)}")

result = decimalToSanafu(sum(result))
print(f"Part 1: {''.join(result)}")