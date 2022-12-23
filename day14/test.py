from day14 import createMapData

testData = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

testMapData = createMapData(testData)

print(f"Height: {testMapData['height']}")
print(f"Min Width: {testMapData['minWidth']}")
print(f"Max Width: {testMapData['maxWidth']}")

for row in testMapData["map"]:
    line = "".join(row)
    print(line)

for n in range(6, 5):
    print(n)
