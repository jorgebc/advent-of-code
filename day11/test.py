from day11 import relief, calculateMonkeyBusinessLevel

testResult = relief(1501)
assert testResult == 500, f"Error in relief 1501, with {testResult}"
testResult = relief(1862)
assert relief(1862) == 620, f"Error in relief 1862, with {testResult}"
testResult = relief(71)
assert relief(71) == 23, f"Error in relief 71, with {testResult}"

monkey0 = {
    "items": [79, 98],
    "operation": lambda worryLevel: worryLevel * 19,
    "test": 23,
    "testTrueMonkey": 2,
    "testFalseMonkey": 3,
    "inspectedItems": 0,
}

monkey1 = {
    "items": [54, 65, 75, 74],
    "operation": lambda worryLevel: worryLevel + 6,
    "test": 19,
    "testTrueMonkey": 2,
    "testFalseMonkey": 0,
    "inspectedItems": 0,
}

monkey2 = {
    "items": [79, 60, 97],
    "operation": lambda worryLevel: worryLevel * worryLevel,
    "test": 13,
    "testTrueMonkey": 1,
    "testFalseMonkey": 3,
    "inspectedItems": 0,
}

monkey3 = {
    "items": [74],
    "operation": lambda worryLevel: worryLevel + 3,
    "test": 17,
    "testTrueMonkey": 0,
    "testFalseMonkey": 1,
    "inspectedItems": 0,
}

testInputData = [monkey0, monkey1, monkey2, monkey3]
rounds = 20
testExpectedResult = 10605
result = calculateMonkeyBusinessLevel(testInputData, rounds, True)
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"

monkey0 = {
    "items": [91, 66],
    "operation": lambda worryLevel: worryLevel * 13,
    "test": 19,
    "testTrueMonkey": 6,
    "testFalseMonkey": 2,
    "inspectedItems": 0,
}

monkey1 = {
    "items": [78, 97, 59],
    "operation": lambda worryLevel: worryLevel + 7,
    "test": 5,
    "testTrueMonkey": 0,
    "testFalseMonkey": 3,
    "inspectedItems": 0,
}

monkey2 = {
    "items": [57, 59, 97, 84, 72, 83, 56, 76],
    "operation": lambda worryLevel: worryLevel + 6,
    "test": 11,
    "testTrueMonkey": 5,
    "testFalseMonkey": 7,
    "inspectedItems": 0,
}

monkey3 = {
    "items": [81, 78, 70, 58, 84],
    "operation": lambda worryLevel: worryLevel + 5,
    "test": 17,
    "testTrueMonkey": 6,
    "testFalseMonkey": 0,
    "inspectedItems": 0,
}

monkey4 = {
    "items": [60],
    "operation": lambda worryLevel: worryLevel + 8,
    "test": 7,
    "testTrueMonkey": 1,
    "testFalseMonkey": 3,
    "inspectedItems": 0,
}

monkey5 = {
    "items": [57, 69, 63, 75, 62, 77, 72],
    "operation": lambda worryLevel: worryLevel * 5,
    "test": 13,
    "testTrueMonkey": 7,
    "testFalseMonkey": 4,
    "inspectedItems": 0,
}

monkey6 = {
    "items": [73, 66, 86, 79, 98, 87],
    "operation": lambda worryLevel: worryLevel * worryLevel,
    "test": 3,
    "testTrueMonkey": 5,
    "testFalseMonkey": 2,
    "inspectedItems": 0,
}

monkey7 = {
    "items": [95, 89, 63, 67],
    "operation": lambda worryLevel: worryLevel + 2,
    "test": 2,
    "testTrueMonkey": 1,
    "testFalseMonkey": 4,
    "inspectedItems": 0,
}

inputData = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
rounds = 20
result = calculateMonkeyBusinessLevel(inputData, rounds, True)
testExpectedResult = 101436
assert (
    result == testExpectedResult
), f"Result should be {testExpectedResult} but was {result}"
print(f"Part 1: {result}")

monkey0 = {
    "items": [79, 98],
    "operation": lambda worryLevel: worryLevel * 19,
    "test": 23,
    "testTrueMonkey": 2,
    "testFalseMonkey": 3,
    "inspectedItems": 0,
}

monkey1 = {
    "items": [54, 65, 75, 74],
    "operation": lambda worryLevel: worryLevel + 6,
    "test": 19,
    "testTrueMonkey": 2,
    "testFalseMonkey": 0,
    "inspectedItems": 0,
}

monkey2 = {
    "items": [79, 60, 97],
    "operation": lambda worryLevel: worryLevel * worryLevel,
    "test": 13,
    "testTrueMonkey": 1,
    "testFalseMonkey": 3,
    "inspectedItems": 0,
}

monkey3 = {
    "items": [74],
    "operation": lambda worryLevel: worryLevel + 3,
    "test": 17,
    "testTrueMonkey": 0,
    "testFalseMonkey": 1,
    "inspectedItems": 0,
}

testInputData = [monkey0, monkey1, monkey2, monkey3]
rounds = 10000
testExpectedResult = 2713310158
# result = calculateMonkeyBusinessLevel(testInputData, rounds, False)
# assert (result == testExpectedResult), f"Result should be {testExpectedResult} but was {result}"

monkey0 = {
    "items": [91, 66],
    "operation": lambda worryLevel: worryLevel * 13,
    "test": 19,
    "testTrueMonkey": 6,
    "testFalseMonkey": 2,
    "inspectedItems": 0,
}

monkey1 = {
    "items": [78, 97, 59],
    "operation": lambda worryLevel: worryLevel + 7,
    "test": 5,
    "testTrueMonkey": 0,
    "testFalseMonkey": 3,
    "inspectedItems": 0,
}

monkey2 = {
    "items": [57, 59, 97, 84, 72, 83, 56, 76],
    "operation": lambda worryLevel: worryLevel + 6,
    "test": 11,
    "testTrueMonkey": 5,
    "testFalseMonkey": 7,
    "inspectedItems": 0,
}

monkey3 = {
    "items": [81, 78, 70, 58, 84],
    "operation": lambda worryLevel: worryLevel + 5,
    "test": 17,
    "testTrueMonkey": 6,
    "testFalseMonkey": 0,
    "inspectedItems": 0,
}

monkey4 = {
    "items": [60],
    "operation": lambda worryLevel: worryLevel + 8,
    "test": 7,
    "testTrueMonkey": 1,
    "testFalseMonkey": 3,
    "inspectedItems": 0,
}

monkey5 = {
    "items": [57, 69, 63, 75, 62, 77, 72],
    "operation": lambda worryLevel: worryLevel * 5,
    "test": 13,
    "testTrueMonkey": 7,
    "testFalseMonkey": 4,
    "inspectedItems": 0,
}

monkey6 = {
    "items": [73, 66, 86, 79, 98, 87],
    "operation": lambda worryLevel: worryLevel * worryLevel,
    "test": 3,
    "testTrueMonkey": 5,
    "testFalseMonkey": 2,
    "inspectedItems": 0,
}

monkey7 = {
    "items": [95, 89, 63, 67],
    "operation": lambda worryLevel: worryLevel + 2,
    "test": 2,
    "testTrueMonkey": 1,
    "testFalseMonkey": 4,
    "inspectedItems": 0,
}
inputData = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
rounds = 10000
result = calculateMonkeyBusinessLevel(inputData, rounds, False)
print(f"Part 2: {result}")
