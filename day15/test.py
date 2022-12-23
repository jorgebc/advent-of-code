import datetime
import os
from day15 import (
    extractSensorBeacon,
    parseSensorBeaconData,
    createSensorBeaconMap,
    calculateRowPositionsCannotContainBeaconWithMap,
    calculateRowPositionsCannotContainBeacon,
)

testData = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


sensorBeaconTestData = """Sensor at x=14, y=17: closest beacon is at x=10, y=16"""
testExpectedResult = {
    "sensorCoords": {"x": 14, "y": 17},
    "beaconCoords": {"x": 10, "y": 16},
    "distances": {"xDistance": 4, "yDistance": 1, "distance": 5},
}
result = extractSensorBeacon(sensorBeaconTestData)
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"

testExpectedResult = 26
result = calculateRowPositionsCannotContainBeaconWithMap(10, testData)
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"

testExpectedResult = 26
result = calculateRowPositionsCannotContainBeacon(10, testData)
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


now = datetime.datetime.now()
print(now)
data = getInputFromFile("day15\\input.txt")
result = calculateRowPositionsCannotContainBeacon(2000000, data)
print(f"Part 1 result: {result}")
now = datetime.datetime.now()
print(now)
